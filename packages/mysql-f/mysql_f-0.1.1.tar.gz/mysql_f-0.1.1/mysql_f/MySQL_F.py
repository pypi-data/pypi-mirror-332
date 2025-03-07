import os
import time
import MySQLdb
from MySQLdb import Error
from functools import wraps
from functools import lru_cache
from dbutils.pooled_db import PooledDB
from typing import Union, List, Dict, Tuple


class MySQL_F:
    def __init__(self, dbName="mydb", tableName="user", host='localhost', user='root', password='root', charset='utf8mb4', poolSize=os.cpu_count() * 5):
        self.table = tableName
        self._logWithIcon('💾 ✅ ', '初始化数据库中...')
        self._initDatabase(dbName, host, user, password, charset)
        self.pool = self._createPool(dbName, host, user, password, charset, poolSize)
        self._maxChunkSize = 500  # 批量插入分块阈值
        self._logWithIcon('🚀 ✅ ', f'数据库就绪 | 连接池: {poolSize}')


    # 耗时统计装饰器
    def _timerDecorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            startTime = time.time()  # 记录开始时间
            result = func(*args, **kwargs)  # 执行函数
            endTime = time.time()  # 记录结束时间
            print(f"执行耗时: {endTime - startTime:.4f} 秒\n")
            return result
        return wrapper


    # 创建数据表（带索引优化）
    @_timerDecorator
    def create(self, columns: Dict[str, str]) -> bool:
        try:
            with self.pool.connection() as conn:
                cursor = conn.cursor()
                cols = ', '.join([f"{k} {v}" for k, v in columns.items()])
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table} ({cols})")
                return True
        except Error as e:
            self._logWithIcon('📝 ❌ ', f'表创建失败: {self.table}', error=e)
            return False


    # 插入数据（智能分块优化）
    @_timerDecorator
    def add(self, data: Union[Dict, List[Dict]]) -> int:
        try:
            result = self._smartInsert(self.table, data)
            self._logWithIcon('📥 ✅ ', f'插入成功: {self.table} | 行数: {result}')
            return result
        except Error as e:
            self._logWithIcon('📥 ❌ ', f'插入失败: {self.table}', error=e)
            return 0


    # 查询数据（带LRU缓存优化）
    @_timerDecorator
    def get(self, where: Dict = None, fields: List[str] = None) -> List[Dict]:
        # 转换参数为可哈希类型
        where_hashable = self._convertToHashable(where)
        fields_hashable = tuple(fields) if fields else None
        return self._queryDataCached(self.table, where_hashable, fields_hashable)


    # 删除数据
    @_timerDecorator
    def dels(self, where: Dict = None) -> int:
        try:
            with self.pool.connection() as conn:
                cursor = conn.cursor()
                if where is None: cursor.execute(f"DELETE FROM {self.table}")
                else:
                    whereClause, params = self._buildWhereClause(where)
                    cursor.execute(f"DELETE FROM {self.table} WHERE {whereClause}", params)
                conn.commit()
                self._logWithIcon('🚮 ✅ ', f'删除成功: {self.table} | 行数: {cursor.rowcount}')
                return cursor.rowcount
        except Error as e:
            self._logWithIcon('🚮 ❌ ', f'删除失败: {self.table}', error=e)
            return 0


    # 条件更新数据
    @_timerDecorator
    def set(self, setData: Dict, where: Dict) -> int:
        try:
            setClause, setParams = self._buildSetClause(setData)
            whereClause, whereParams = self._buildWhereClause(where)
            with self.pool.connection() as conn:
                cursor = conn.cursor()
                sql = f"UPDATE {self.table} SET {setClause} WHERE {whereClause}"
                cursor.execute(sql, setParams + whereParams)
                conn.commit()
                self._logWithIcon('🔄 ✅ ', f'更新成功: {self.table} | 行数: {cursor.rowcount}')
                return cursor.rowcount
        except Error as e:
            self._logWithIcon('🔄 ❌ ', f'更新失败: {self.table}', error=e)
            return 0


    # 执行原生SQL
    @_timerDecorator
    def sql(self, sql: str, args: tuple = None) -> Union[int, List[Dict]]:
        try:
            with self.pool.connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, args or ())
                if sql.strip().upper().startswith("SELECT"):
                    results = self._formatResults(cursor)
                    self._logWithIcon('⚡ ✅ ', f'SQL查询完成 | 结果数: {len(results)}')
                    return results
                else:
                    conn.commit()
                    self._logWithIcon('⚡ ✅ ', f'SQL执行成功 | 影响行数: {cursor.rowcount}')
                    return cursor.rowcount
        except Error as e:
            self._logWithIcon('⚡ ❌ ', 'SQL执行失败', error=e)
            return 0


    @lru_cache(maxsize=1024)
    def _queryDataCached(self, tableName: str, where_hashable: tuple, fields_hashable: tuple) -> List[Dict]:
        # 转换回原始参数类型
        where = dict(where_hashable) if where_hashable else None
        fields = list(fields_hashable) if fields_hashable else None
        
        # 原有的查询逻辑
        try:
            selectFields = '*' if not fields else ','.join(fields)
            whereClause, params = self._buildWhereClause(where) if where else ('1=1', [])
            with self.pool.connection() as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT {selectFields} FROM {tableName} WHERE {whereClause}", params)
                results = self._formatResults(cursor)
                self._logWithIcon('🔍 ✅ ', f'查询完成: {tableName} | 结果数: {len(results)}')
                return results
        except Error as e:
            self._logWithIcon('🔍 ❌ ', f'查询失败: {tableName}', error=e)
            return []


    # 将字典或列表转换为可哈希的类型
    def _convertToHashable(self, data: Union[Dict, List]) -> Union[tuple, None]:
        if isinstance(data, dict): return tuple(sorted(data.items()))
        elif isinstance(data, list): return tuple(data)
        elif data is None: return None
        else: raise TypeError(f"不可哈希的类型: {type(data)}")


    # 单条插入优化
    def _singleInsert(self, tableName: str, data: Dict) -> int:
        with self.pool.connection() as conn:
            cursor = conn.cursor()
            keys = data.keys()
            values = tuple(data.values())
            placeholders = ','.join(['%s'] * len(keys))
            cursor.execute(
                f"INSERT INTO {tableName} ({','.join(keys)}) VALUES ({placeholders})", 
                values
            )
            conn.commit()
            return cursor.rowcount


    # 智能插入策略
    def _smartInsert(self, tableName: str, data: Union[Dict, List[Dict]]) -> int:
        if isinstance(data, list):
            chunkSize = self._calcDynamicChunkSize(data)
            total = 0
            for i in range(0, len(data), chunkSize):
                total += self._bulkInsert(tableName, data[i:i+chunkSize])
            return total
        else:
            return self._singleInsert(tableName, data)


    # 高效批量插入
    def _bulkInsert(self, tableName: str, chunk: List[Dict]) -> int:
        with self.pool.connection() as conn:
            cursor = conn.cursor()
            keys = chunk[0].keys()
            values = [tuple(d.values()) for d in chunk]
            sql = f"INSERT INTO {tableName} ({','.join(keys)}) VALUES ({','.join(['%s']*len(keys))})"
            cursor.executemany(sql, values)
            conn.commit()
            return cursor.rowcount


    # 动态计算分块大小
    def _calcDynamicChunkSize(self, data: List[Dict]) -> int:
        if not data: return self._maxChunkSize
        sampleSize = min(10, len(data))
        avgSize = sum(len(str(d)) for d in data[:sampleSize]) // sampleSize
        maxPacket = 4 * 1024 * 1024  # 默认4MB限制
        return min(self._maxChunkSize, maxPacket // (avgSize or 1))


    # 增强型条件构建
    def _buildWhereClause(self, where: Dict) -> Tuple[str, List]:
        clauses, params = [], []
        for k, v in where.items():
            if v is None:
                clauses.append(f"{k} IS NULL")
            elif isinstance(v, list):
                clauses.append(f"{k} IN ({','.join(['%s']*len(v))})")
                params.extend(v)
            elif isinstance(v, tuple) and len(v) == 2:  # 支持范围查询
                operator, value = v
                clauses.append(f"{k} {operator} %s")
                params.append(value)
            else:
                clauses.append(f"{k}=%s")
                params.append(v)
        return " AND ".join(clauses), params


    # 增强型SET构建
    def _buildSetClause(self, setData: Dict) -> Tuple[str, List]:
        clauses, params = [], []
        for k, v in setData.items():
            clauses.append(f"{k}=%s")
            params.append(v)
        return ", ".join(clauses), params


    # 初始化数据库
    def _initDatabase(self, dbName: str, host: str, user: str, password: str, charset: str) -> None:
        try:
            conn = MySQLdb.connect(host=host, user=user, password=password, charset=charset)
            with conn.cursor() as cursor: cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbName}")
            conn.commit()
        except Error as e:
            self._logWithIcon('📥 ❌ ', '数据库初始化失败', error=e)
            raise


    # 创建优化后的连接池       
    def _createPool(self, dbName: str, host: str, user: str, password: str, charset: str, poolSize: int):
        return PooledDB(
            creator=MySQLdb,
            mincached=2,
            maxconnections=poolSize,
            host=host,
            user=user,
            passwd=password,
            db=dbName,
            charset=charset,
            cursorclass=MySQLdb.cursors.DictCursor
        )


    # 统一格式化结果
    def _formatResults(self, cursor) -> List[Dict]:
        return [dict(row) for row in cursor.fetchall()]


    # 日志输出
    def _logWithIcon(self, icon: str, message: str, error: Exception = None):
        logMsg = f"{icon} {message}"  # 构造日志消息，包含图标和消息内容
        if error: logMsg += f" | 错误: {str(error)}"
        print(f"[{time.strftime('%H:%M:%S')}] {logMsg}")
