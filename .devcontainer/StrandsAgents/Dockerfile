# CircleCIのPythonイメージをベースにする
FROM cimg/python:3.11

# CircleCIイメージは既にsudo権限を持つ 'circleci' ユーザーが含まれています
# 必要に応じてシステムパッケージを追加
USER root
RUN apt-get update && apt-get install -y \
    # Strands Agentなどでブラウザ操作が必要な場合はここに追加
    && rm -rf /var/lib/apt/lists/* && arch=$(uname -m) && \
    if [ "$arch" != "x86_64" ]; then \
        arch="aarch64"; \
    fi && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-${arch}.zip" -o "aws-cli.zip" && \
    unzip aws-cli.zip && \
    sudo ./aws/install && \
    rm -rf aws aws-cli.zip
USER circleci
