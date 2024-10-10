import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@ssossosso'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 피드 항목 개수 출력
print(f"Number of entries in feed: {len(feed.entries)}")
for entry in feed.entries:
    print(f"Entry title: {entry.title}")

    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title.replace('/', '-').replace('\\', '-') + '.md'
    file_path = os.path.join(posts_dir, file_name)

    # 파일이 이미 존재하지 않으면 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)  # 글 내용을 파일에 작성
            print(f"Created file: {file_path}")  # 파일 생성 확인용 로그

        # 깃허브에 파일 추가
        repo.git.add(file_path)
        print("After adding file, Git status:")
        print(repo.git.status())

# Git 상태 확인 및 커밋
if repo.index.diff("HEAD"):
    repo.git.commit('-m', f'Add post: {entry.title}')
    print(f"Committed: {entry.title}")
else:
    print('No changes to commit.')

# 변경 사항을 깃허브에 푸시
repo.git.push()
