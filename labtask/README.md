## 实验室任务管理系统

### 1. 数据库设计
项目信息表

| 字段         | 类型      |  含义    |
| :--------:   | :-----:   | :----: |
| project_id |  int   |   项目id    |
| project_name | varchar  |   项目名称     |
| owner | int      | 项目负责人，user外键    |
|project_status| int| 项目当前状态 |
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
|task_status| int| 任务当前状态 |
| project_id | int | 任务所属项目 |
| start_time | datetime | 任务开始时间 |
| end_time | datetime | 任务结束时间 |


### 2. 模块功能

#### 2-1 项目申请

    申请项目需要填写项目名称、申请人、项目简介、开始及结束时间等重要信息，并填写项目下的子任务及子任务相关信息。

#### 2-2 项目编辑

    包括项目预计时间修改、状态修改、完成情况等内容的编辑修改。

#### 2-3 项目查看

    项目状态的查看，检索项目、内容搜索等。
    
#### 2-4 项目总结

    项目、任务结束时记录总结信息。

#### 2-5 统计数据

    按时间、数量、人物等维度展示项目的统计数据。








