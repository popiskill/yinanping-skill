#!/usr/bin/env python3
"""
意难平 Skill - 人物档案读写工具
用于保存、读取、列表、删除模拟人物档案
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# 档案存储目录
PERSONAS_DIR = Path(__file__).parent.parent / "personas"


def ensure_dir():
    """确保档案目录存在"""
    PERSONAS_DIR.mkdir(parents=True, exist_ok=True)


def save_persona(name: str, data: dict) -> dict:
    """保存人物档案"""
    ensure_dir()
    
    # 添加元数据
    data["meta"] = {
        "name": name,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "version": 1
    }
    
    # 文件名安全处理
    safe_name = "".join(c for c in name if c.isalnum() or c in "._-").strip()
    if not safe_name:
        safe_name = f"persona_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    filepath = PERSONAS_DIR / f"{safe_name}.json"
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return {
        "status": "ok",
        "name": name,
        "path": str(filepath),
        "message": f"人物档案 '{name}' 已保存"
    }


def load_persona(name: str) -> dict:
    """读取人物档案"""
    ensure_dir()
    
    # 尝试精确匹配
    filepath = PERSONAS_DIR / f"{name}.json"
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {
            "status": "ok",
            "data": data
        }
    
    # 尝试模糊匹配
    for f in PERSONAS_DIR.glob("*.json"):
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            if data.get("meta", {}).get("name") == name:
                return {
                    "status": "ok",
                    "data": data
                }
    
    return {
        "status": "error",
        "message": f"未找到人物档案: {name}"
    }


def list_personas() -> dict:
    """列出所有人物档案"""
    ensure_dir()
    
    personas = []
    for f in PERSONAS_DIR.glob("*.json"):
        try:
            with open(f, "r", encoding="utf-8") as fp:
                data = json.load(fp)
                meta = data.get("meta", {})
                personas.append({
                    "name": meta.get("name", f.stem),
                    "relation": data.get("relation", "未知"),
                    "timeframe": data.get("timeframe", "未知"),
                    "created_at": meta.get("created_at", "未知"),
                    "summary": data.get("summary", "")[:50] + "..." if data.get("summary") else ""
                })
        except Exception as e:
            personas.append({
                "name": f.stem,
                "error": str(e)
            })
    
    return {
        "status": "ok",
        "count": len(personas),
        "personas": personas
    }


def delete_persona(name: str) -> dict:
    """删除人物档案"""
    ensure_dir()
    
    # 尝试精确匹配
    filepath = PERSONAS_DIR / f"{name}.json"
    if filepath.exists():
        filepath.unlink()
        return {
            "status": "ok",
            "message": f"人物档案 '{name}' 已删除"
        }
    
    # 尝试模糊匹配
    for f in PERSONAS_DIR.glob("*.json"):
        try:
            with open(f, "r", encoding="utf-8") as fp:
                data = json.load(fp)
                if data.get("meta", {}).get("name") == name:
                    f.unlink()
                    return {
                        "status": "ok",
                        "message": f"人物档案 '{name}' 已删除"
                    }
        except:
            pass
    
    return {
        "status": "error",
        "message": f"未找到人物档案: {name}"
    }


def update_persona(name: str, updates: dict) -> dict:
    """更新人物档案"""
    result = load_persona(name)
    if result["status"] != "ok":
        return result
    
    data = result["data"]
    
    # 合并更新
    def deep_merge(base, new):
        for key, value in new.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                deep_merge(base[key], value)
            else:
                base[key] = value
    
    deep_merge(data, updates)
    
    # 更新元数据
    data["meta"]["updated_at"] = datetime.now().isoformat()
    data["meta"]["version"] = data["meta"].get("version", 1) + 1
    
    # 保存
    return save_persona(name, data)


def main():
    """CLI 入口"""
    if len(sys.argv) < 2:
        print(json.dumps({
            "status": "error",
            "message": "用法: persona_writer.py <action> [args...]",
            "actions": ["save", "load", "list", "delete", "update"]
        }))
        sys.exit(1)
    
    action = sys.argv[1]
    
    if action == "save":
        if len(sys.argv) < 4:
            print(json.dumps({"status": "error", "message": "用法: persona_writer.py save <name> <json_data>"}))
            sys.exit(1)
        name = sys.argv[2]
        data = json.loads(sys.argv[3])
        result = save_persona(name, data)
        
    elif action == "load":
        if len(sys.argv) < 3:
            print(json.dumps({"status": "error", "message": "用法: persona_writer.py load <name>"}))
            sys.exit(1)
        result = load_persona(sys.argv[2])
        
    elif action == "list":
        result = list_personas()
        
    elif action == "delete":
        if len(sys.argv) < 3:
            print(json.dumps({"status": "error", "message": "用法: persona_writer.py delete <name>"}))
            sys.exit(1)
        result = delete_persona(sys.argv[2])
        
    elif action == "update":
        if len(sys.argv) < 4:
            print(json.dumps({"status": "error", "message": "用法: persona_writer.py update <name> <json_updates>"}))
            sys.exit(1)
        name = sys.argv[2]
        updates = json.loads(sys.argv[3])
        result = update_persona(name, updates)
        
    else:
        result = {
            "status": "error",
            "message": f"未知操作: {action}"
        }
    
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
