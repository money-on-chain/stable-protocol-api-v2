# Stable Protocol API v2

## Warning: This is only for version 2 of the main contracts.

API list operations of the users dapp. This is a requirement for [stable-protocol-interface-v2](https://github.com/money-on-chain/stable-protocol-interface-v2), this service list operations of the users.

### Usage

Requirements:

* Python 3.9+
* Mongo DB installed also DB, User & pass created
* [Stable-protocol-indexer-v2](https://github.com/money-on-chain/stable-protocol-indexer-v2)Protocol Indexer installed & Running in the same Mongo DB

```
# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
copy environments/development/.example.env .env

# Edit .env file and change settings point Mongo DB uris 

# Start the service
uvicorn api.app:app --reload
```

### Interactive API docs

Go to http://localhost:8000/


### Deployed environments


| Environment   | Project   | URL                                    | 
|---------------|-----------|----------------------------------------|
| Testnet       | Flipmoney | https://api-testnet.flipmoney.io/      |
| Mainnet       | Flipmoney | https://api-v2.flipmoney.io/           |
| Testnet       | ROC       | https://api-v2-testnet.rifonchain.com/ |
| Mainnet       | ROC       | https://api-v2.rifonchain.com/         |

### Docker (Recommended)

Build, change path to correct environment

```
docker build -t stable_protocol_api_v2 -f Dockerfile.api .
```

Run

```
docker run -d \
--name stable_protocol_api_v2_roc_mainnet \
--env APP_MONGO_URI=mongodb://localhost:27017 \
--env APP_MONGO_DB=roc_mainnet \
--env BACKEND_CORS_ORIGINS=["*"] \
--env ALLOWED_HOSTS=["*"] \
--env VENDOR_ADDRESS=0xC61820bFB8F87391d62Cd3976dDc1d35e0cf7128 \
--env COMMISSION_SPLITTER_V2=0xce4548BC0b865197D94E15a5440299398aB9d32E
stable_protocol_api_v2
```


