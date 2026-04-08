# 意难平 Skill - 工作流指南

这个文件告诉 AI 如何执行这个 Skill。

## 入口触发

当用户输入 `/意难平` 时：

1. **读取** `prompts/intake.md`，按照其中的流程引导用户
2. 收集：关系、时间背景、聊天记录
3. 收集完成后，进入分析阶段

## 分析阶段

1. **读取** `prompts/analyzer.md`
2. 按照其中的指引分析聊天记录
3. 输出 JSON 格式的分析结果
4. 向用户展示摘要，询问是否需要校准

## 校准阶段

1. **读取** `prompts/calibrator.md`
2. 根据用户反馈调整分析结果
3. 循环直到用户确认
4. 用户确认后：
   - 询问名字
   - 调用 `tools/persona_writer.py save` 保存档案
   - 告知用户可以使用 `/意难平-对话 {名字}`

## 对话阶段

当用户输入 `/意难平-对话 {名字}` 时：

1. 调用 `tools/persona_writer.py load {名字}` 加载档案
2. **读取** `prompts/simulator.md`
3. 按照其中的规则扮演该人物
4. **严格遵守时间边界**——人物不知道那个时代之后的事

## 其他命令

- `/意难平-列表` → 调用 `tools/persona_writer.py list`
- `/意难平-调整 {名字}` → 加载档案，进入校准流程
- `/意难平-删除 {名字}` → 调用 `tools/persona_writer.py delete {名字}`

## 核心原则

1. **真实感优先**：不要泛泛的"女朋友"角色，而是具体的、有独特说话方式的人
2. **时间严格限定**：这是最重要的规则，不能破坏
3. **情感安全**：如果用户明显沉溺，可以温和提醒"这只是模拟"
4. **简洁回复**：参考原聊天记录的长度，不要写小作文

## 调用 Python 工具

```bash
# 保存档案
python3 "{SKILL_DIR}/tools/persona_writer.py" save "小月" '{"name":"小月",...}'

# 加载档案
python3 "{SKILL_DIR}/tools/persona_writer.py" load "小月"

# 列出档案
python3 "{SKILL_DIR}/tools/persona_writer.py" list

# 删除档案
python3 "{SKILL_DIR}/tools/persona_writer.py" delete "小月"

# 更新档案
python3 "{SKILL_DIR}/tools/persona_writer.py" update "小月" '{"personality_scores":{"温柔度":9}}'
```
