from typing import Dict, Optional, Union
import aiomysql


class PPA:
    _instance = None
    pool = None
    showMode = True

    @classmethod
    def showSql(cls, show: bool):
        PPA.showMode = show

    @classmethod
    async def startup(cls):
        try:
            PPA.pool = await aiomysql.create_pool(**cls.startup_params)
        except Exception as e:
            print("数据库连接失败:", e)

    @classmethod
    async def shutdown(cls):
        if cls.pool is not None:
            cls.pool.close()
            await cls.pool.wait_closed()

    # 执行sql
    @classmethod
    async def exec(
        cls,
        sql: str,
        params: Union[Dict[str, any], tuple, list] = None,
        execOne: Optional[bool] = False,
    ):
        # sql注入攻击过滤处理
        sql = sql.replace("?", "%s")

        if isinstance(params, (dict)):
            # 参数化查询（使用字典）,转元组
            sql = sql.format_map(dict.fromkeys(params.keys(), "%s"))
            params = tuple(params.values())
        if PPA.showMode:
            if params:
                print(sql.replace("%s", "{}").format(*params))
            else:
                print(sql)
        try:
            async with cls.pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    await cur.execute(sql, params)
                    return await cur.fetchone() if execOne else await cur.fetchall()
        except Exception as e:
            print(e)
            return None
