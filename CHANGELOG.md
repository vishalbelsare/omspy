### 0.19.1
### Fixes
* Same memory id for `PegExisting` order. See #21
* Negative mtm for trailing algo fixed #49
### 0.19.0
### Breaking Changes
* **Kotak** broker removed. Deprecated code available at [omspy-brokers](https://github.com/uberdeveloper/omspy-brokers)
### Features
* New algo for trailing added in `algos/trailing`
* New broker `Noren` added
### Improvements
* `FakeBroker` return formats improved. See #42
* All brokers must return orders as empty list if no orders are found (instead of a dictionary inside list or other format)
### Fixes
* exch_tm error fixed for `Finvasia` broker #46.
* `ReplicaBroker` not to raise error if instruments not available #41.

### 0.18.2
### Fixes
* average_price for `FakeBroker` would take care of None values in price or trigger_price
### 0.18.1
### Fixes
* #45 Type conversion fixed
* Deprecation message added for inactive broker modules
### Improvments
* #41 return order_id only
### 0.18.0
### Features
 * STOP order simulation added to `OrderFill` #40
 * `utils.load_broker` to automatically load broker from credentials file
### Improvements
 * finvasia broker upgraded to Norenapi version 0.3
 * #38 All brokers to be initialized to None
 * #39 All broker connections to be done only during authentication
 * extra attribute added to yaml files for all brokers
 * `pytop` library added to main dependency

### Fixes
 * `orders` property for all brokers to return empty list in case of errors (no empty dictionary inside list)
 * **Neo** broker `orders` property to infer side automatically
 * **Icici** broker proper data conversion for orders
 * #35 when both random numbers are same, the end number is changed automatically to prevent raising error
### 0.17.4
### Fixes
 * side added to `orders` property in `Neo` broker
### 0.17.3
### Improvements
 * `Neo` broker authentication improved to automatically store session token and retry next time
### Fixes
 * `MARKET` order in order placement in `Neo` broker is now automatically adjusted
 * `order_place` and `order_modify` methods in `Neo` broker to automatically adjust correct order type
### 0.17.2
### Fixes
 * Deprecation notice added to Kotak broker
 * Neo broker `order_place` method to automatically correct order type and trading symbol
### 0.17.1
Bug fix for zerodha broker headless mode
### 0.17.0
Better support for latest python version and broker improvements
### Features
* New broker `ICICI` added
### Improvements
* selenium dependency removed and replaced with nodriver
* pendulum upgraded to version 3.0
* packages upgraded for python version 3.10 and above
* brokers ~`Fyers`~ and ~`MasterTrust`~ removed

### 0.16.4
* `Kotak` broker updated for latest master format

### 0.16.3
* Dependencies updated to match python3.10 and above
### 0.16.1
### Improvements
* `VOrder` can now accept string as order types like MARKET/LIMIT in addition to `OrderType` Enum
* `Kotak` broker exchange_timestamp in orders would datetime objects instead of pendulum objects
### 0.16.0
### Features
* `ReplicaBroker` class added to simulation to replicate order fills based on real broker data
### Improvements
* `print` replaced with `logging` for zerodha broker

### 0.15.0
### Features
* New broker `Neo` added

### 0.14.2
Improvements to `FakeBroker` module
### Features
* user can provide a custom response to all methods in `FakeBroker` if you pass a response keyword argument
* `side` to be converted to enum even if passed as a BUY or SELL string
* fake methods added for `orders` and `trades`

### 0.14.1
### Fixes
* kotak broker `instrument_master` extra columns bug fixed - broker added extra columns for a few instruments to track market surveillance

### 0.14.0
Improvements to the VirtualBroker module
### Features
Following features added to `VirtualBroker`
* `VirtualBroker` methods to match `FakeBroker` methods
* Users added, orders can be placed and managed based on user
* Order status could be fetched based on Status
* delay attribute added to broker
* Ticker model improved with ohlc and orderbook methods

### Improvements
* `iterate_method` made generic
* `Ticker` model now moved to models

### 0.13.0
* New `FakeBroker` class added to simulation
* API added for generating fake data in `omspy.simulation.server`

### 0.12.0
### Features
* New `simulation` module added
* `VirtualBroker` added for faking orders
* You can now add keys to `CompoundOrder` when adding an order
* `CompoundOrder` orders now have an automatic index
* `get` function added to `CompoundOrder` to search by index or custom key
* `update_quantity` function added to utils

### 0.11.0
### Features
* `force_order_type` directive added to `PegSequential` orders; now `PegSequential` orders could either force order type to LIMIT or proceed with the actual order type

### Fixes
* kotak broker `close_all_positions` correctly implemented
* kotak broker price and trigger price to be set to zero when MARKET order is placed

### 0.10.2
### Fixes
* zerodha broker TOTP auto login error fixed

### 0.10.1
### Fixes
* zerodha broker `side` forced to be in upper case to enable `close_all_positions`

### 0.10.0
### Features
* order `execute, modify, cancel` functions to take additional attribs_to_copy argument to copy attributes from brokers
* Broker instance could have now have properties to be added automatically during `execute, modify, cancel` function

### Fixes
* Finvasia broker to return order_id as a string instead of dictionary
* Finvasia broker `order_modify` to correctly add arguments when called

### 0.9.1
### Fixes
* Finvasia broker to suffix EQ to orders only when the exchange is NSE
### Improvement
* Finvasia broker - more columns converted to proper types
* Kotak broker - more columns converted
### Internals
* Kotak broker `create_instrument_master` to fetch dataframe from a different function, the new function is added for better modularity

## 0.9.0
### Features
* `TrailingStopOrder` added to stop orders
* `TargetOrder` added to stop orders
* `BracketOrder` removed from stop orders

### Improvements
* `StopOrder` and `StopLimitOrder` model changed

### Fixes
* Kotak broker exchange_timestamp format handled correctly
* Finvasia broker exchange and broker timestamp format handled correctly
* Timestamp for kotak, finvasia brokers to be saved in db in expected format

## 0.8.3
### Features
* `close_all_positions` could take a symbol_transformer function to transform symbols
* `close_all_positions` can take positions as an optional argument; this would help in passing select positions to square off instead of closing all positions
* `PegExisting` and `PeqSequential` can now take `modify_args` to add any extra broker arguments needed when modifying orders

### Improvements
* `close_all_positions` to handle errors and valid quantity of any type
* type conversion done for data received from broker `Finvasia`
* #9 when an `Order` is added to `CompoundOrder` add an id automatically if there is no id
* #25 `PegSequential` order lock mechanism now dependent on `add_lock` method for each order; so each order could have its own order lock.

### Fixes
* #15 do not update `Order` if order `is_done` (completed/rejected/canceled)

### Internals
* tests improved for `Order` class


## 0.8.2
### Improvements
* Instrument master for broker `kotak` could be generated for any combination of columns
* `modify` order could now take extra attributes to be passed on to broker
* tests rewritten with `PurePath` and other refactoring, credits to @soumyarai2050 for pushing these changes

### Fixes
* Instrument master for  broker `kotak` to handle strike prices till 3 decimal places (for currency strikes)
* `modify_order` for broker `kotak` to correctly handle order types, especially MARKET

## 0.8.1
### Improvements
* TOTP authentication added to Finvasia broker
* TOTP autentication added to MasterTrust broker

## 0.8.0
### Features
* New `OrderStrategy` class added, an abstraction over CompoundOrder
* OrderLock mechanism added to `Order` so that each order would have its own unique lock

## 0.7.1
This is a bug-fix version and enhancement version

### Fixes
* #20 You can now pass order arguments to `PegExisting` and `PegSequential`
* #18 timezone to default to local instead of UTC
* #11 pending quantity to be automatically updated

## 0.7.0
### Features
* CandleStick class added to models
* Cancel subsequent orders in `PegSequential` if one of the orders fail

### Improvements
* `is_done` method added to `Order` - returns True when the order is either complete or canceled or rejected.
* cancel peg orders after expiry

### Fixes
* `order_cancel` not to be called when no  order_id is None

## 0.6.1
### Improvements
* Extra order mappings for SLM and SLL added to finvasia broker
* `order_type` argument resolved for kotak broker

## 0.6.0
### Features
* Broker support added for **finvasia**
* New order type `PegSequential` added to peg orders in sequence

## 0.5.1
### Improvements
* Order Lock mechanism added
* ExistingPeg to check for time expiry before next peg

## 0.5.0
### Features
* ExistingPeg order added to peg existing orders

### Features
* Broker support added for **kotak**

## 0.4.0

### Features
* **BREAKING CHANGE:** Database structured changed. New keys added
* new **multi** module added for placing the same order for multiple clients

### Fixes
* #13 do not change existing timestamp fixed
* cloning an order creates a new timestamp instead of the original one
* keyword arguments passed to `modify` method to update order attributes and then modify the broker order
* peg order attributes carried to child orders

## 0.3.0

### Features
* new **peg order module** added for peg orders.
* peg to market order added with basic arguments
* new **models** module added. This contains basic model for converting and manipulating data
* new **utils** module added that contains utility and helper functions. Functions added
	* create_basic_positions_from_orders_dict
	* dict_filter
	* tick
	* stop_loss_step_decimal
* mandatory arguments for order placement for zerodha broker added. `order_place, order_modify, order_cancel` would now add default arguments for the broker automatically (such as variety);you could override them with kwargs.
* cover_orders function added to broker class, this checks for all valid orders and place stop loss in case of non-matching orders


## 0.2.0

### Features
* **BREAKING CHANGE:** Database model changed
* `Order, CompoundOrder` models changed from dataclass to pydantic models
* database class changed to sqlite_utils from native python sqlite3 for better reading and writing, connection now returns `sqlite_utils.Database` instead of `sqlite3.Connection`.
* #3 `Order` could now be directly added using the `add` method and this inherits the sqlite3 database from the compound order if no connection is specified
* #8 save method added to save orders to database in bulk
* #6 maximum limit for modifications to an order added

### Fixes
* close_all_positions bug fixed by changing status to upper case and including canceled and rejected orders in completed orders
* cancel_all_orders do not cancel already completed orders

### Internals

* `_attrs` now made part of model instead of a property
* tests updated to reflect the new database type


## 0.1.4
* modify order to accept any parameter

## 0.1.3
* save to database on execution

## 0.1.2
* fixes in brokers
* order arguments during execution in compound orders

## 0.1.1
* database support for saving orders added
