# lecoCramming
互助刷题 互相监督， 每周至少保持N天的刷题。
## 参与repo方式
0. fork一个自己的仓库，然后发起Pull Request到组长的分支。所有更新操作在自己分支完成。
1. clone自己fork的分支；或者直接GitHub页面上新增文件，在线编辑
2. 本地以自己的姓名或昵称为名称新建分支，这样不会引起冲突
3. 同样命名方式新建文件夹
4. 每天写好打卡的题目后，题目文件放入自己的文件夹，之后本地commit，再发起pull request。

## 目录
- [同时设置github和gitlab](#同时设置github和gitlab)
- [将一个已存在的目录转换为一个 GIT 项目并托管到 GITHUB 仓库](#将一个已存在的目录转换为一个 GIT 项目并托管到 GITHUB 仓库)
- [在不下载已有分支文件的情况下推送到新分支](#在不下载已有分支文件的情况下推送到新分支)
- [只下载部分文件](#只下载部分文件)


git 教程 https://segmentfault.com/a/1190000003728094 

# 同时设置github和gitlab  
https://www.cnblogs.com/lfr0123/p/13477001.html   
```bash
cd ~/.ssh
ls
ssh-keygen -t rsa -f ~/.ssh/[id_rsa_xxxxxxxxxxx] -C "email.com"
ssh-add ~/.ssh/id_rsa_1
ssh-add ~/.ssh/id_rsa_2
sudo gedit config
```
将pub文件中的内容贴到帐号的ssh管理中  
将以下内容粘贴到config里
```
# 自己的github账号配置
Host github.com
	HostName github.com
	PreferredAuthentications publickey
	IdentityFile ~/.ssh/id_rsa_github

# 公司的gitlab账号配置(HostName为公司的gitlab地址)
Host git.de
	User 真实user名
	HostName git.de
	PreferredAuthentications publickey
	IdentityFile ~/.ssh/id_rsa_XXXX
```
然后用以下语句验证，不需要修改@前边的git
```
ssh -T git@github.com
ssh -T git@git.....
```
如果还是有问题，检查私钥文件权限和所有权
```
chmod 600 ~/.ssh/id_rsa_RWTH-ce
sudo chown $(whoami) ~/.ssh/id_rsa_XXX
```
```sh
git config --local user.name 'username' #github账号名称
git config --local user.email 'username@gmail.com' #github账号邮箱
```
```
# 确保在本地 main 分支上
git checkout main

# 推送本地 main 分支到远端的 hiwi 分支
git push origin main:hiwi
```
# 将一个已存在的目录转换为一个 GIT 项目并托管到 GITHUB 仓库  
https://blog.csdn.net/solo_ws/article/details/77095901

使用yml升级环境  
`conda update conda`  
`conda activate xxx`  
`conda env update --file env-ids-ws23.yml --prune`  


docker 不用每次加sudo  
https://www.cnblogs.com/jzcn/p/16591083.html

Cmake的使用  
https://www.cnblogs.com/pandamohist/p/16890474.html


# 在不下载已有分支文件的情况下推送到新分支
你可以使用 Git 在不下载已有分支文件的情况下，将新文件夹的内容推送到一个已存在仓库的新的分支中。以下是具体步骤：

步骤一：初始化本地仓库
在新文件夹中初始化 Git 仓库：

```sh
cd path/to/your/new/folder
git init
```
添加远程仓库：

```sh
git remote add origin https://github.com/yourusername/yourrepository.git
```
步骤二：创建并切换到新分支
创建并切换到新分支：
```sh
git checkout -b new-branch-name
```
步骤三：添加文件并提交
添加新文件夹中的所有内容：

```sh
git add .
```
提交更改：

```sh
git commit -m "Initial commit for new branch"
```
步骤四：推送新分支到远程仓库
推送新分支到远程仓库：
```sh
git push origin new-branch-name
```

# 只下载部分文件
```sh
# 初始化并设置远程
git init myrepo
cd myrepo
git remote add origin https://github.com/username/repo.git

# 设置稀疏检出
git sparse-checkout init --cone
git sparse-checkout set data/Git/task/

# 拉取main分支
git pull origin main

# 确保切换到master分支
git checkout master

# 创建目标目录
mkdir -p ./data/Git/task/

# 创建新文件并写入内容
echo "【大家可以叫我】your-nickname" > ./data/Git/task/camp3_xxx.md

# 添加新文件到Git
git add ./data/Git/task/camp3_xxx.md

# 提交新文件
git commit -m "Add new file camp3_xxx.md"

# 推送本地master分支到远程的camp3分支
git push origin master:camp3
```
