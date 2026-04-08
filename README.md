<div align="center">

# 🥀 意难平

**把「意难平」变成一场跨时空对话**

上传你和 TA 的聊天记录，AI 学习 TA 的性格，模拟「如果在一起」会怎样

[![GitHub stars](https://img.shields.io/github/stars/popiskill/yinanping-skill?style=social)](https://github.com/popiskill/yinanping-skill/stargazers)
[![GitHub license](https://img.shields.io/github/license/popiskill/yinanping-skill)](https://github.com/popiskill/yinanping-skill/blob/main/LICENSE)

<img src="./assets/banner.png" alt="意难平 Banner" width="100%">

</div>

---

## ✨ 核心功能

| 功能 | 说明 |
|------|------|
| 🎭 **性格学习** | 基于真实聊天记录，学习 TA 的说话风格 |
| ⏰ **时间限定** | 严格限定时代背景，不会聊未来的事 |
| 🎯 **精准校准** | 5 维性格参数可调（听话度/傲娇度/活跃度/温柔度/调皮度）|
| 💾 **持久化存储** | 创建的人物档案永久保存 |

---

## 🚀 快速开始

### 安装

```bash
# 克隆到 OpenClaw skills 目录
git clone https://github.com/popiskill/yinanping-skill ~/.qclaw/workspace/skills/yinanping
```

### 使用

```
/意难平
```

然后按提示操作即可。

---

## 📖 使用流程

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  选择关系   │ ──▶ │  选择时间   │ ──▶ │ 上传聊天   │ ──▶ │  开始对话   │
│  暗恋/前任  │     │  高中/大学  │     │  记录/记忆  │     │  模拟 TA    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

---

## 💬 支持的关系类型

| 类型 | 说明 |
|------|------|
| 💭 **暗恋对象** | 从未表白，想模拟「如果表白了」|
| 💔 **前任** | 曾经在一起，想回到那段时光 |
| 🌙 **错过的缘分** | 暧昧过但没结果 |
| 🤝 **好友/兄弟** | 想再次和 TA 聊天 |
| 👨‍👩‍👧 **亲人** | 想念逝去的亲情 |
| 👤 **一面之缘** | 那个擦肩而过的人 |

---

## 🎨 示例对话

**场景**：高中时代的前女友

```
你：在干嘛
TA：刷剧呢 无聊

你：出来玩吗
TA：还要写作业呢...

你：想你了
TA：...
```

---

## ⚠️ 注意事项

- 🚫 **时代严格限定**：2018 年的人不会知道疫情
- 💡 **聊天记录越详细，还原度越高**
- ❤️ **这是疗愈，不是沉溺**

---

## 📁 文件结构

```
yinanping/
├── SKILL.md          # Skill 入口
├── prompts/          # 提示词模板
│   ├── intake.md     # 初始问询
│   ├── analyzer.md   # 性格分析
│   ├── calibrator.md # 用户校准
│   └── simulator.md  # 对话模拟
└── tools/            # 工具脚本
    └── persona_writer.py
```

---

<div align="center">

## 📄 License

MIT License - 自由使用，欢迎 Fork

**Made with ❤️ by [popiskill](https://github.com/popiskill)**

</div>
