## 实验室任务管理系统

### 1. 数据库设计
项目信息表

| 字段         | 类型      |  含义    |
| :--------:   | :-----:   | :----: |
| project_id |  int   |   项目id    |
| project_name | varchar  |   项目名称     |
| owner_id | int      | 项目负责人，user外键    |
|project_info| varchar| 项目简介 |
|start_time | datetime | 项目开始时间 |
|end_time | datetime | 项目结束时间 |

任务信息表

| 字段         | 类型      |  含义    |
| :--------:   | :-----:   | :----: |
| task_id |  int   |   任务id    |
| task_name | varchar  |   任务名称     |
| owner_id | int      | 负责人，user外键   |
| task_info | varchar| 任务简介 |
| project_id | int | 任务所属项目 |
| start_time | datetime | 任务开始时间 |
| end_time | datetime | 任务结束时间 |





