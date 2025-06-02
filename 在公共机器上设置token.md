# 📘 GitHub 私有仓库操作笔记（在公用电脑 / 无用户隔离环境）

## 🎯 目标

在 **共用 Windows 电脑（RDP 登录、共用账号）** 上：

- ✅ 使用 Git 操作自己的 GitHub **私有仓库**
- ✅ 不影响或泄露其他用户凭据
- ✅ 不让别人用你的身份 `push` 或 `pull`
- ✅ **每次操作手动输入你的 GitHub Token**

---

## 🔐 一、你能实现什么功能？

- ✅ 安全地 clone、pull、push 你的 private repo
- ✅ 不污染其他人的全局 Git 配置
- ✅ 不保存你的 token，不留痕迹
- ✅ 即使别人也在这台电脑上用 Git，也互不影响

---

## 🔍 二、查看系统是否已有 Git 设置（别人留下的）

```bash
# 查看全局配置
git config --global --list

# 查看凭据缓存是否启用
git config --global credential.helper

# 查看是否有默认用户名（可能是别人的）
git config --global user.name
git config --global user.email
```

---

## 🧼 三、清理干扰你的“系统级凭据缓存”（跳过这步，不清楚会不会影响别人）

### Step 1：禁用全局凭据缓存（不删除别人的账号，只不使用）

```bash
git config --global --unset credential.helper
```

### Step 2：手动清除已保存的 GitHub 凭据（可选）

- 打开 Windows 控制面板 → 用户账户 → **凭据管理器** → **Windows 凭据**
- 删除名称为：
  ```
  git:https://github.com
  ```
  的条目（如果它是别人的）

---

## 🔑 四、生成 GitHub Token（代替密码使用）

1. 打开：https://github.com/settings/tokens
2. 点击 `Generate new token (classic)`
3. 设置：
   - 名称：任意（如 `public-windows-access`）
   - 有效期：建议 30 天
   - 勾选权限：✅ `repo`
4. 点击“生成” → **复制 Token，一次性显示，保存好！**

---

## 📥 五、克隆私有仓库（强制使用你自己的身份）

```bash
git clone https://your-username@github.com/your-username/your-repo.git
```

> ✅ 这样可以**强制 Git 提示输入你的 Token**
> 
> ```
> Username: your-username
> Password: <粘贴你的 Token>
> ```

🛑 不要使用 `your-username:your-token@...` 的方式，容易暴露 Token！  
🛑 成功之后还要回到Windows 控制面板 → 用户账户 → **凭据管理器** → **Windows 凭据**，删除掉记录，不然会留`https://your-username@github.com/`的记录
---

## 🧷 六、克隆成功后设置本项目为“隔离配置”（局部配置）

进入你的项目目录后，执行：

```bash
# 只影响当前项目，不影响别人
git config user.name "Your Name"
git config user.email "your@email.com"
git config credential.helper ""
```

效果：

- ✅ 所有 Git 操作会提示你手动输入 token
- ✅ 不会使用或保存别人（或你）的 GitHub 凭据

---

## 🔁 七、之后如何使用 Token？

在任何一次 `push/pull` 时，Git 会提示：

```bash
Username: your-username
Password: <粘贴你保存的 Token>
```

你只需手动粘贴即可。**不会被保存**，也不会自动重用。

---

## 🧠 附：推荐命令汇总

```bash
# 设置本项目使用你的用户名
git config user.name "Your Name"
git config user.email "your@email.com"

# 禁用凭据缓存（只对当前项目）
git config credential.helper ""

# 强制用你自己的身份 clone 私有仓库
git clone https://your-username@github.com/your-username/your-repo.git
```

---

## ✅ 总结建议

| 项目 | 推荐设置 |
|------|-----------|
| Token 权限 | 仅勾选 `repo` |
| Token 保存 | 不保存，手动粘贴最安全 |
| Git 凭据 | 禁用全局 helper，用项目局部配置 |
| 克隆地址 | 用 `your-username@github.com/...` 格式，避免触发别人凭据 |

---

## ✅ 建议你避开的做法（尤其在公用电脑）

| 做法 | 原因 |
|------|------|
| 设置 `--global user.name/email` | 会污染别人提交记录 |
| 使用 SSH key | 私钥无法安全保存 |
| 使用 `credential.helper manager` | 会保存你的 token，别人可用 |
| 把 token 放进 URL | 容易泄露到日志、`.git/config` |
