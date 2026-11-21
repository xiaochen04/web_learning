from datetime import date

from base import Base
from database import engine, SessionLocal
from models import Employee,Department #必须要加

# 创建表
def create_table():
     print("注册的表名:", Base.metadata.tables.keys())
     # 创建所有模型对应的表
     Base.metadata.create_all(bind=engine)
     print("表创建成功")


def insert_data():
    # 获取数据库会话
    db = SessionLocal()

    try:
        # =========== 第一步：新增部门 =============
        new_dept = Department(
            name="研发部",  # 部门名称（唯一）
            location="北京总部"  # 部门位置
        )
        db.add(new_dept)  # 将部门对象加入会话
        db.commit()  # 提交到数据库（执行 INSERT 语句）
        db.refresh(new_dept)  # 刷新对象，获取自增的 id 等字段
        print(new_dept.id,new_dept.name,new_dept.location)

        # =========== 第二步：新增关联的员工 ===========
        # 员工1：关联上面创建的研发部
        emp1 = Employee(
            name="张三",
            age=30,
            hire_date=date(2023, 1, 1),  # 入职日期（datetime.date 类型）
            department_id=new_dept.id  # 关联部门 ID（外键）
        )
        # 员工2：同部门的另一个员工
        emp2 = Employee(
            name="李四",
            age=28,
            hire_date=date(2023, 3, 15),
            department_id=new_dept.id
        )

        # 批量添加员工（也可逐个 add）
        db.add_all([emp1, emp2])
        db.commit()  # 提交员工数据
        # 刷新员工对象，获取自增 ID
        db.refresh(emp1)
        db.refresh(emp2)


    except Exception as e:
        db.rollback()  # 出错时回滚
        print(f"新增失败：{e}")
    finally:
        db.close()  # 关闭会话

def delete_data():
    # 获取会话
    session = SessionLocal()

    try:
        # 删除单个员工
        emp = session.query(Employee).filter(Employee.name == "李四").first()
        if emp:
            session.delete(emp)
            session.commit()
            print(f"已删除员工：{emp.name}")

    except Exception as e:
        session.rollback()  # 出错时回滚
        print(f"刪除失败：{e}")
    finally:
        session.close()  # 关闭会话

def update_data():
    # 获取会话
    session = SessionLocal()
    try:
        # 修改员工年龄
        emp = session.query(Employee).filter(Employee.name == "张三").first()
        if emp:
            emp.age = 31  # 直接修改属性
            session.commit()  # 提交更新
            print(f"修改后 {emp.name} 的年龄：{emp.age}")

    except Exception as e:
        session.rollback()  # 出错时回滚
        print(f"修改失败：{e}")
    finally:
        session.close()  # 关闭会话

def read_data():
    # 获取会话
    session = SessionLocal()
    try:
        # ======按主键查询 get========
        #  查询id=1的部门
        dept = session.get(Department,1)
        print(f"部门 ID=1：{dept.name}（{dept.location}）")

        # ======过滤（filter）查询========
        # 查询研发部的所有员工
        rd_employees = session.query(Employee).filter(
            Employee.department_id == 1  # 按部门ID过滤
        ).all()
        print("研发部员工：", [emp.name for emp in rd_employees])  # 输出：['张三']

    except Exception as e:
        session.rollback()  # 出错时回滚
        print(f"查询失败：{e}")
    finally:
        session.close()  # 关闭会话


if __name__ == '__main__':
    # create_table()
    # insert_data()
    # delete_data()
    # update_data()
    read_data()