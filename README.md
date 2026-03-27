# Strands Agents

## Setup

```bash
aws configure sso --profile default
```

リージョンは`ap-northeast-1`、出力形式は`json`にします。

```bash
export AWS_DEFAULT_REGION=us-west-2
```

```bash
aws sts get-caller-identity
```

## Run

デフォルトではus-west-2のClaude 4 Sonnetが使われます。
bedrockのモデルを使う場合はstrands.modelsというパッケージからBedrockModelクラスをインポートします。

## Run A2A

```bash
pip install --user --break-system-packages 'strands-agents[a2a]' strands-agents-tools
```

## Google ADK Setup

```bash
curl -sSL https://sdk.cloud.google.com | bash && exec -l $SHELL && gcloud init
```

setup gcloud.

```bash
gcloud auth login
gcloud auth application-default login
```

Set the project ID.

```bash
gcloud config set project $PROJECT_ID
```

Setup environment variables.

```bash
export GOOGLE_CLOUD_PROJECT=`gcloud config list --format 'value(core.project)'`
export GOOGLE_CLOUD_LOCATION=us-central1
```

```bash
pip install --user --break-system-package google-adk
```

## option

Setup `.env` file.

```bash
echo "GOOGLE_GENAI_USE_VERTEXAI=TRUE" > ./multi_tool_agent/.env
echo "GOOGLE_CLOUD_LOCATION=us-central1" >> ./multi_tool_agent/.env
echo "GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT" >> ./multi_tool_agent/.env
```

## トラブルシューティング

503エラーが発生する場合は、agent cardのURLが正しいか、サーバーが起動しているかを確認してください。

```text
Error: HTTP Error 503: Network communication error fetching agent card from http://localhost:9000/.well-known/agent-card.json: All connection attempts failed
```

## reference

- [strands-agents/tools](https://github.com/strands-agents/tools)
- [Welcome - Strands Agents](https://strandsagents.com/latest/documentation/docs/)
