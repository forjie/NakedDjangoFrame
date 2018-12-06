import os

import MySQLdb
from django.conf import settings
from django.core.management.base import BaseCommand

from stp.envirement import ENVIRONMENT
from .util import connect
from comm.argument import apps


def find_migrations(base_dir):
    """查找 migrations 文件"""
    for dirpath, dirnames, filenames in os.walk(base_dir):
        print(dirpath, 1, dirnames, 2, filenames, 3)
        if not dirpath.endswith('migrations'):
            continue

        for file_name in filenames:
            if file_name != '__init__.py':
                yield os.path.join(dirpath, file_name)


def del_db(cursor, database_name):
    """删除数据库"""
    try:
        print(f"start drop datebase {database_name}...")
        cursor.execute(f"DROP DATABASE {database_name}")
        print(f"drop datebase {database_name} done!")
    except Exception as e:
        print(
            f"""can't drop datebase {database_name},
            please make sure the {database_name} exist!
            the program will try to create the {database_name}
            """
        )


def add_db(cursor, database_name):
    """添加数据库"""
    try:
        print(f"start create datebase {database_name}...")
        cursor.execute(
            f"""
            CREATE DATABASE {database_name}
            CHARACTER SET=utf8mb4 collate=utf8mb4_general_ci
            """
        )
        print(f"create datebase {database_name} done!")
    except MySQLdb.ProgrammingError:
        print(
            f"can't create datebase {database_name}, the {database_name} may already exist!"
        )


def main(flag):
    for file_name in find_migrations(apps):
        os.remove(file_name)

    database = settings.DATABASES
    db = database['default']['NAME']
    user = database['default']['USER']
    password = database['default']['PASSWORD']
    host = database['default']['HOST']
    port = database['default']['PORT']

    cursor = connect(user, password, host, port)
    if not flag:
        del_db(cursor, db)
        add_db(cursor, db)
        print("rebuild database done!")


class Command(BaseCommand):
    def add_arguments(self, parser):
        """覆盖基类，增加命令行参数
        """
        parser.add_argument(
            '--migrations', action='store_true', dest='migrations',
            help="regenerate the migrations file"
        )

    def handle(self, *args, **options):
        if ENVIRONMENT != 'local' and ENVIRONMENT != 'dev':
            print('the rebuild_db commands only the local environment to use!')
            return
        flag = options.get('migrations')
        main(flag)

        # 当参数中有migrations,直接建表
        if flag:
            from django.core.management import execute_from_command_line
            execute_from_command_line(["manage.py", "makemigrations"])
            execute_from_command_line(["manage.py", "migrate"])


if __name__ == '__main__':
    main()
