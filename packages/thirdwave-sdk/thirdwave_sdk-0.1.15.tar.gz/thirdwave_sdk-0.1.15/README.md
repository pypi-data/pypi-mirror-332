# Python SDK for Thirdwave's API

Python client for interacting with the Thirdwave wallet intelligence API over gRPC

## Installation

Install the SDK using pip:

```zsh
pip install thirdwave-sdk
```

## Usage

Retrieving information about wallet or list of wallets
```python
import nest_asyncio
import asyncio
from thirdwave_sdk import ThirdwaveClient

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()


async def main():
    # Initialize the client
    thirdwave_client = ThirdwaveClient(api_key="MY-API-KEY", options={"transport_type": "secure"})
    await thirdwave_client.initialize()

    # Get a single wallet
    wallet_result = await thirdwave_client.wallet.get_one("0x0...")
    print("Single Wallet Result:", wallet_result)

    # Get multiple wallets
    wallet_list = ["0x0...", "0x0..."]
    async for wallet in thirdwave_client.wallet.get_many(wallet_list):
        print("Wallet from List:", wallet)

    # Close the client
    await thirdwave_client.close()


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
```

Retrieving information about Erc20 and Native tokens meta-data
```python
import nest_asyncio
import asyncio

from thirdwave_sdk.client import ThirdwaveClient

nest_asyncio.apply()


async def main():
    # Initialize the client
    thirdwave_client = ThirdwaveClient(api_key="MY-API-KEY", options={"transport_type": "secure"})
    await thirdwave_client.initialize()

    wallet_list = ["0x0...", "0x0..."]

    # Using set to work only with unique token identifiers
    native_tokens_set = set()
    erc_20_tokens_set = set()
    
    async for wallet in thirdwave_client.wallet.get_many(wallet_list):
        native_tokens_set.update(item.blockchain_id for item in wallet.native_token_holdings if item is not None)
        erc_20_tokens_set.update((item.blockchain_id, item.address) for item in wallet.erc20_token_holdings if item is not None)

    async for data in thirdwave_client.wallet.get_native_tokens_metadata(native_tokens_set):
        print("Native token data: ", data)

    async for data in thirdwave_client.wallet.get_erc20_tokens_metadata(erc_20_tokens_set):
        print("Erc20 token data: ", data)

    # Close the client
    await thirdwave_client.close()


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
```

#### WalletService

The ThirdwaveClient class utilizes the WalletService to interact with the EVM Wallet service over gRPC. The WalletService provides methods for retrieving wallet information, streaming multiple wallets, and adding a wallet via a gRPC stream.

##### Attributes

channel: The gRPC channel used to communicate with the EVM Wallet service.
api_key: The API key for authenticating requests.
stub: The gRPC stub for the EVM Wallet service.

##### Initialization

__init__(self, channel, api_key: str)
Initializes the WalletService.

##### Parameters:

* channel: The gRPC channel to the EVM Wallet service.
* api_key (str): The API key to authenticate requests.

##### Methods:
###### async get_one(self, address: str | bytes) -> EvmWallet
Retrieves the information for a single wallet by address.

##### Parameters:

* address (str | bytes): The wallet address in string or bytes format.

##### Returns:

* EvmWallet: The wallet object containing the details of the wallet.

##### Raises:

[grpc.RpcError](https://grpc.io/docs/guides/status-codes/): If the gRPC call fails.

###### async get_many(self, addresses: List[str] | List[bytes]) -> AsyncGenerator[EvmWallet, None]
Streams information for multiple wallets given a list of addresses.

##### Parameters:

* addresses (List[str] | List[bytes]): A list of wallet addresses in string or bytes format.

##### Yields:
  EvmWallet: The wallet object for each address in the list.

##### Raises:

  [grpc.RpcError](https://grpc.io/docs/guides/status-codes/): If the gRPC call fails.

---

### Dev Prerequisites

- [Python >=3.10](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)

### Setup virtual environment with `direnv` or poetry env

You can set up the virtual environment using either `direnv` or Poetry directly. Alternatively, you can set up a Poetry virtual environment by running `make venv`.

#### Setting Up Direnv

1. **Install `direnv`**:

Follow the [installation instructions](https://direnv.net/docs/installation.html) for your operating system.

2. Add this to `~/.direnvc`

   ```bash
   layout_poetry() {
     if [[ ! -f pyproject.toml ]]; then
       log_error 'No pyproject.toml found.  Use `poetry new` or `poetry init` to create one first.'
       exit 2
     fi

     local VENV=$(dirname $(poetry run which python))
     export VIRTUAL_ENV=$(echo "$VENV" | rev | cut -d'/' -f2- | rev)
     export POETRY_ACTIVE=1
     PATH_add "$VENV"
   }
   ```

3. **Create `.envrc`**:

   Create a `.envrc` file in the root of the project with the following content:

   ```sh
   layout poetry
   ```

#### Using Poetry to setup a virtual environment

To set up the virtual environment and install dependencies:

```
poetry env use python3.12
```

#### Setup Poetry and Install dependencies with `make install`

#### Update protocol buffers to the latest version

First remove existing protos with `make clean_proto`

```
make clean_proto
```

#### Pull latest proto files and build python stubs

```
make proto
```

#### Generate new proto files with `make proto`

Ensure that the generated code produced correct import paths, python's grpcio tools are not maintained as well as other languages and often generate code with broken imports
