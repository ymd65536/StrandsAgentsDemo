# CircleCIのPythonイメージをベースにする
FROM cimg/python:3.11

# CircleCIイメージは既にsudo権限を持つ 'circleci' ユーザーが含まれています
# 必要に応じてシステムパッケージを追加
USER root
RUN apt-get update && apt-get install -y \
    # Strands Agentなどでブラウザ操作が必要な場合はここに追加
    && rm -rf /var/lib/apt/lists/*

USER circleci
