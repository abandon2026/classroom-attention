# 课堂专注度分析系统 - 接口规范文档 V1.0
基于多任务CNN的课堂专注度智能分析系统，实时检测学生人脸、头部姿态、课堂行为与表情，生成班级专注度报告，辅助教师提升教学效果。

## 技术栈
- 算法：Python, OpenCV, MTCNN, YOLOv8, 6D-RepNet
- 后端：Flask, SQLite
- 前端：PyQt5
- 协作：Git, GitHub

## 团队分工
| 角色                            | 负责人                 | 核心职责                                     |
|---------------------------|---------------------|----------------------------------------|
| 技术队长                     | xxx                     | Git仓库管理、接口文档、代码规范  |
| 算法A（人脸+姿态）    | xxx                     | 人脸检测、头部姿态估计                |
| 算法B（行为+表情）    | xxx                     | 行为识别、表情分类                      |
| 后端开发                     | xxx                     | Flask API、数据库接口                  |
| 前端开发                     | xxx                     | PyQt5界面、数据可视化                |

## 快速开始
1. 克隆仓库：`git clone https://github.com/abandon2026/classroom-attention.git`
2. 安装依赖：`pip install -r requirements.txt`
3. 启动后端：`python src/api/app.py`
4. 启动前端：`python src/gui/main.py`
## 一、统一数据格式

### 1.1 人脸信息格式
```json
{
    "face_id": "student_001",
    "bbox": [x, y, width, height],
    "landmarks": {
        "left_eye": [x, y],
        "right_eye": [x, y],
        "nose": [x, y],
        "left_mouth": [x, y],
        "right_mouth": [x, y]
    },
    "confidence": 0.95
}
1.2 头部姿态格式
{
    "face_id": "student_001",
    "pitch": 12.5,
    "yaw": 8.3,
    "roll": 2.1,
    "attention_level": "专注听课"
}
1.3 行为检测格式
{
    "face_id": "student_001",
    "behavior": "举手",
    "confidence": 0.85
}
1.4 表情识别格式
{
    "face_id": "student_001",
    "emotion": "专注",
    "confidence": 0.78
}
1.5 专注度评分格式
{
    "face_id": "student_001",
    "attention_score": 85,
    "level": "高专注度"
}
二、模块接口定义
2.1 算法A：人脸检测模块
文件位置: src/face/detector.py

python
class FaceDetector:
    def detect(self, frame: np.ndarray) -> List[Dict]:
        """
        输入: BGR格式图像
        输出: 人脸信息列表，格式见 1.1
        """
        pass
2.2 算法A：头部姿态模块
文件位置: src/face/pose.py

python
class HeadPoseEstimator:
    def estimate(self, face_img: np.ndarray, landmarks: Dict) -> Dict:
        """
        输入: 人脸图像 + 关键点
        输出: 姿态信息，格式见 1.2
        """
        pass
2.3 算法B：行为检测模块
文件位置: src/behavior/detector.py

python
class BehaviorDetector:
    def detect(self, frame: np.ndarray, face_bbox: List[int]) -> Dict:
        """
        输入: 整帧图像 + 人脸框
        输出: 行为信息，格式见 1.3
        """
        pass
2.4 算法B：表情识别模块
文件位置: src/behavior/emotion.py

python
class EmotionRecognizer:
    def predict(self, face_img: np.ndarray) -> Dict:
        """
        输入: 人脸图像
        输出: 表情信息，格式见 1.4
        """
        pass
2.5 专注度评分模块
文件位置: src/behavior/scorer.py

python
class AttentionScorer:
    def calculate(self, pose: Dict, behavior: Dict, emotion: Dict) -> Dict:
        """
        输入: 姿态+行为+表情
        输出: 专注度评分，格式见 1.5
        """
        pass
三、后端API接口
3.1 处理单帧图像
请求

text
POST /api/process_frame
Content-Type: application/json
json
{
    "frame": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
}
响应

json
{
    "code": 200,
    "msg": "success",
    "data": {
        "frame": "data:image/jpeg;base64,/9j/4AAQSkZJRg...",
        "students": [
            {
                "face_id": "001",
                "bbox": [100, 150, 80, 80],
                "attention_score": 85,
                "behavior": "写笔记",
                "emotion": "专注",
                "pose": {"pitch": 12.5, "yaw": 8.3, "roll": 2.1}
            }
        ],
        "class_stats": {
            "avg_score": 72.5,
            "student_count": 25,
            "low_attention_count": 3
        }
    },
    "timestamp": "2024-03-25 10:30:00"
}
3.2 获取课堂报告
请求

text
GET /api/get_report?class_id=001
响应

json
{
    "code": 200,
    "msg": "success",
    "data": {
        "class_name": "计算机视觉",
        "date": "2024-03-25",
        "avg_attention": 72.5,
        "attention_distribution": {
            "high": 15,
            "medium": 10,
            "low": 3
        }
    }
}
四、开发规范
4.1 函数命名
使用 snake_case

示例：detect_faces(), calculate_score()

4.2 类命名
使用 PascalCase

示例：FaceDetector, BehaviorDetector

4.3 返回值
统一使用 Dict 或 List[Dict]

不要返回自定义对象

4.4 错误处理
出错时返回 None 或空列表

不要抛出异常

五、版本记录
版本	  日期	        修改内容	   修改人
V1.0	  2024-03-25	初稿创建	   梁连赢
V1.1	  待定	        待讨论	-