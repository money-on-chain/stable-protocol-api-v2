# exit as soon as an error happen
set -e

usage() { echo "Usage: $0 -e <environment> -i <aws id> -r <aws region>" 1>&2; exit 1; }

while getopts ":e:i:r:" o; do
    case "${o}" in
        e)
            e=${OPTARG}
            ((  e=="flipago_testnet" || e=="flipago_mainnet" || e == "roc_testnet" || e == "roc_mainnet" )) || usage
            case $e in
                flipago_testnet)
                    ENV=$e
                    ;;
                flipago_mainnet)
                    ENV=$e
                    ;;
                roc_testnet)
                    ENV=$e
                    ;;
                roc_mainnet)
                    ENV=$e
                    ;;
                *)
                    usage
                    ;;
            esac
            ;;
        i)
            i=${OPTARG}
            AWS_ID=$i
            ;;
        r)
            r=${OPTARG}
            AWS_REGION=$r
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

if [ -z "${e}" ] || [ -z "${i}" ] || [ -z "${r}" ]; then
    usage
fi

docker image build -t stable-protocol-api-v2_$ENV -f ./Dockerfile.api .

echo "Build done!"

# login into aws ecr
$(aws ecr get-login --no-include-email --region $AWS_REGION)

echo "Logging to AWS done!"

docker tag stable-protocol-api-v2_$ENV:latest $AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com/stable-protocol-api-v2_$ENV:latest

docker push $AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com/stable-protocol-api-v2_$ENV:latest

echo "finish done!"