# from XTConnect import XTSConnect
from Connect import XTSConnect

"Note : For dealer credentials add the clientID and for investor client leave the clientID blank"


"""Interactive client credentials"""
API_KEY = ""
API_SECRET = ""
clientID = ""
userID = ""
source = "WEBAPI"

"""Make XTSConnect object by passing your interactive API appKey, secretKey and source"""
xt = XTSConnect(API_KEY, API_SECRET, source)

#hostlookuplogin
hostlookupres = xt.hostlookup_login()

"""Using the xt object we created call the interactive login Request"""
response = xt.interactive_login()
print("Login: ", response)


"""Order book Request"""
response = xt.get_order_book()
print("Order Book: ", response)

"""Place Order Request"""
response = xt.place_order(
    exchangeSegment=xt.EXCHANGE_NSECM,
    exchangeInstrumentID=2885,
    productType=xt.PRODUCT_MIS,
    orderType=xt.ORDER_TYPE_MARKET,
    orderSide=xt.TRANSACTION_TYPE_BUY,
    timeInForce=xt.VALIDITY_DAY,
    disclosedQuantity=0,
    orderQuantity=10,
    limitPrice=0,
    stopPrice=0,
    orderUniqueIdentifier="454845",
    apiOrderSource="abc")
print("Place Order: ", response)


# extracting the order id from response
if response['type'] != 'error':
    OrderID = response['result']['AppOrderID']

    """Modify Order Request"""
    response = xt.modify_order(
        appOrderID=OrderID,
        modifiedProductType=xt.PRODUCT_NRML,
        modifiedOrderType=xt.ORDER_TYPE_LIMIT,
        modifiedOrderQuantity=8,
        modifiedDisclosedQuantity=0,
        modifiedLimitPrice=1405,
        modifiedStopPrice=0,
        modifiedTimeInForce=xt.VALIDITY_DAY,
        orderUniqueIdentifier="454845"
    )
    print("Modify Order: ", response)

    """Cancel Orders Request"""
    response = xt.cancel_order(
        appOrderID=OrderID,
        orderUniqueIdentifier='454845')
    print("Cancel Order: ", response)

    """Get Order History Request"""
    response = xt.get_order_history(appOrderID=OrderID)
    print("Order History: ", response)

"""Get Profile Request"""
response = xt.get_profile()
print("Profile: ", response)

"""Get Balance Request"""
response = xt.get_balance()
print("Balance: ", response)

"""Get Trade Book Request"""
response = xt.get_trade()
print("Trade Book: ", response)

"""Get Holdings Request"""
response = xt.get_holding()
print("Holdings: ", response)

"""Get Position by DAY Request"""
response = xt.get_position_daywise()
print("Position by Day: ", response)

"""Get Position by NET Request"""
response = xt.get_position_netwise()
print("Position by Net: ", response)

"""Position Convert Request"""
response = xt.convert_position(
    exchangeSegment=xt.EXCHANGE_NSECM,
    exchangeInstrumentID=2885,
    targetQty=10,
    isDayWise=True,
    oldProductType=xt.PRODUCT_MIS,
    newProductType=xt.PRODUCT_NRML)
print("Position Convert: ", response)

"""Place Cover Order Request"""
response = xt.place_cover_order(
    exchangeSegment=xt.EXCHANGE_NSECM,
    exchangeInstrumentID=2885,
    orderSide=xt.TRANSACTION_TYPE_BUY,
    orderType=xt.ORDER_TYPE_LIMIT,
    orderQuantity=2,
    disclosedQuantity=0,
    limitPrice=1802,
    stopPrice=1899,
    orderUniqueIdentifier="454845",
    apiOrderSource="abc")
print("Cover Order:", response)

# extracting the order id from response
if response['type'] != 'error':
    OrderID = response['result']['ExitAppOrderID']

"""Exit Cover Order Request"""
response = xt.exit_cover_order(appOrderID=OrderID)
print("Exit Cover Order:", response)

"""Place BracketOrder Request"""
response = xt.place_bracketorder(
    exchangeSegment=xt.EXCHANGE_NSECM,
    exchangeInstrumentID=2885,
    orderType=xt.ORDER_TYPE_MARKET,
    orderSide=xt.TRANSACTION_TYPE_BUY,
    disclosedQuantity=0,
    orderQuantity=10,
    limitPrice=59,
    squarOff=1,
    stopLossPrice=1,
	trailingStoploss=1,
    isProOrder=False,
    apiOrderSource="abc",
    orderUniqueIdentifier="454845"
    )
print("Bracket Order: ", response)

# extracting the order id from response
if response['type'] != 'error':
    OrderID = response['result']['AppOrderID']
    
    """Cancel BracketOrder Request"""
    res = xt.bracketorder_cancel(OrderID)
    print("Bracket Cancel: ", response)

    """Modify BracketOrder Request"""
    response = xt.modify_order(
        appOrderID=OrderID,
        orderQuantity=8,
        limitPrice=1405,
        stopPrice=0
    )
    print("Modify BracketOrder: ", response)



"""Regular MarginDetails Request"""
response = xt.margindetails(
        exchangeSegment = xt.EXCHANGE_NSECM,
        exchangeInstrumentID = 2885,
        productType = xt.PRODUCT_MIS,
        orderType = xt.ORDER_TYPE_MARKET,
        orderside = xt.TRANSACTION_TYPE_BUY,
        orderQuantity = 10,
        price = 1000,
        stopPrice = 1200,
        orderSessionType = "NORMAL",
        clientID = clientID
    )
print("Margin Details: ", response)

"""Modify Margin Request"""
response = xt.modifyordermargindetails(
        exchangeSegment = xt.EXCHANGE_NSECM,
        exchangeInstrumentID = 2885,
        orderside = xt.TRANSACTION_TYPE_BUY,
        orderSessionType = "NORMAL",
        productType = xt.PRODUCT_MIS,
        orderType = xt.ORDER_TYPE_MARKET,
        orderQuantity = 10,
        price = 1001,
        stopPrice = 1200,
        orderID = "1548498",
        clientID=clientID
)

"""Cover Order Margin"""
response = xt.comargindetails(
        exchangeSegment = xt.EXCHANGE_NSECM,
        exchangeInstrumentID = 2885,
        orderside = xt.TRANSACTION_TYPE_BUY,
        orderType = xt.ORDER_TYPE_MARKET,
        orderQuantity = 10,
        price = 1000,
        stopPrice = 1200,
        requestId = 1,
        clientID=clientID
)

"""Modify Cover Order Margin"""
response = xt.comodifymargindetails(
        exchangeSegment = xt.EXCHANGE_NSECM,
        exchangeInstrumentID = 2885,
        orderside = xt.TRANSACTION_TYPE_BUY,
        orderType = xt.ORDER_TYPE_MARKET,
        orderQuantity = 10,
        price = 1000,
        stopPrice = 1200,
        requestId = 1,
        orderID = "1546516516",
        clientID=clientID
)

"""Bracket Order Margin Request"""
response = xt.bomargindetails(
        exchangeSegment = xt.EXCHANGE_NSECM,
        exchangeInstrumentID = 2885,
        orderside = xt.TRANSACTION_TYPE_BUY,
        entryorderType = xt.ORDER_TYPE_MARKET,
        orderQuantity = 10,
        limitPrice = 1000,
        squarOff = 1290,
        stopLoss = 1150,
        clientID=clientID
)


"""Place Spread Order"""
response = xt.place_spread_order(
        exchangeSegment = xt.EXCHANGE_NSEFO,
        exchangeInstrumentID = "14590176",
        productType = xt.PRODUCT_NRML,
        orderType = xt.ORDER_TYPE_LIMIT,
        orderDuration = xt.VALIDITY_DAY,
        orderQuantity  = "75",
        spreadPrice = 149,
        leg1ExchangeSegment = xt.EXCHANGE_NSEFO,
        leg1ExchangeInstrumentID = 56785,
        leg2ExchangeSegment = xt.EXCHANGE_NSEFO,
        leg2ExchangeInstrumentID = 53216,
        spreadExchangeInstrumentID = 14590176,
        apiOrderSource = "WEB",
        clientID = clientID,
        userID = userID
)

"""Modify Spread Order"""
response = xt.modify_spread_order(
        exchangeOrderID = "1240970517",
        productType = xt.PRODUCT_NRML,
        orderType = xt.PRODUCT_NRML,
        orderDuration = xt.VALIDITY_DAY,
        orderQuantity = "75",
        spreadPrice = 149,
        apporderID = OrderID,
        leg1ExchangeSegment = xt.EXCHANGE_NSEFO,
        leg1ExchangeInstrumentID = 56785,
        leg2ExchangeSegment = xt.EXCHANGE_NSEFO,
        leg2ExchangeInstrumentID = 53216,
        spreadExchangeInstrumentID = 14590176,
        apiOrderSource = "WEB",
        clientID=clientID
)

"""Get Spread Order Book"""
response = xt.get_spread_order(
    accountID = clientID
)

"""Cancel Spread Order"""
response = xt.cancel_order(
    spreadExchangeSegment = xt.EXCHANGE_NSEFO, 
    spreadExchangeInstrumentID = 56785, 
    exchangeOrderID = 1240970517, 
    appOrderID = 1240970517
)


"""Place GTT Order Request"""
response = xt.place_gtt_order(
        exchangeSegment=xt.EXCHANGE_NSECM,
        exchangeInstrumentID=22,
        productType=xt.PRODUCT_CNC,
        orderType=xt.ORDER_TYPE_LIMIT,
        orderSide=xt.TRANSACTION_TYPE_BUY,
        timeInForce=xt.VALIDITY_DAY,
        disclosedQuantity=0,
        orderQuantity=10,
        limitPrice=1001,
        stopPrice=1200,
        orderUniqueIdentifier="1548498",
        userID=userID,
        clientID = clientID
)

"""Modify GTT Order Request"""
response = xt.modify_gtt_order(
        orderSessionType="GTT",
        exchangeInstrumentID=22,
        exchangeSegment=xt.EXCHANGE_NSECM,
        appOrderID=123456789,
        modifiedLimitPrice=1002,
        orderCategoryType="NORMAL",
        modifiedOrderType=xt.ORDER_TYPE_LIMIT,
        modifiedProductType=xt.PRODUCT_CNC,
        modifiedOrderQuantity=10,
        modifiedStopPrice= 1200,
        participationCode = "None"
)

"""GET GTTT Order Request"""
response = xt.get_gtt_order(clientID=clientID)

"""Cancel GTT Order Request"""
response = xt.cancel_gtt_order(
    appOrderID = 123456789,
    exchangeSegment = xt.EXCHANGE_NSECM, 
    exchangeInstrumentID = 22, 
    clientID = clientID, 
    userID = userID)


"""Cancel all Orders Request"""
response = xt.cancelall_order(exchangeInstrumentID=22,exchangeSegment=xt.EXCHANGE_NSECM)
print("Cancel all Orders: ", response)

"""Interactive logout Request"""
response = xt.interactive_logout(clientID=clientID)
print("Interactive Logout: ", response)

exit()


# ----------------------------------------------------------------------------------------------------------------------
# Marketdata
# ----------------------------------------------------------------------------------------------------------------------

#Marketdata client credentials
API_KEY = ""
API_SECRET = ""
userID = ""
XTS_API_BASE_URL = "https://developers.symphonyfintech.in"
source = "WEBAPI"


"""Make the XTSConnect Object with Marketdata API appKey, secretKey and source"""
xt = XTSConnect(API_KEY, API_SECRET, source)

"""Using the object we call the login function Request"""
response = xt.marketdata_login()
print("MarketData Login: ", response)

"""Get Config Request"""
response = xt.get_config()
print('Config :', response)

"""instruments list"""
instruments = [
    {'exchangeSegment': 1, 'exchangeInstrumentID': 2885},
    {'exchangeSegment': 1, 'exchangeInstrumentID': 22}]

"""Get Quote Request"""
response = xt.get_quote(
    Instruments=instruments,
    xtsMessageCode=1502,
    publishFormat='JSON')
print('Quote :', response)

"""Send Subscription Request"""
response = xt.send_subscription(
    Instruments=instruments,
    xtsMessageCode=1502)
print('Subscribe :', response)

"""Send Unsubscription Request"""
response = xt.send_unsubscription(
    Instruments=instruments,
    xtsMessageCode=1502)
print('Unsubscribe :', response)

"""Get Master Instruments Request"""
exchangesegments = [xt.EXCHANGE_NSECM, xt.EXCHANGE_NSEFO]
response = xt.get_master(exchangeSegmentList=exchangesegments)
print("Master: " + str(response))

"""Get OHLC Request"""
response = xt.get_ohlc(
    exchangeSegment=xt.EXCHANGE_NSECM,
    exchangeInstrumentID=22,
    startTime='Dec 16 2019 090000',
    endTime='Dec 18 2019 150000',
    compressionValue=1)
print("OHLC: " + str(response))

"""Get Series Request"""
response = xt.get_series(exchangeSegment=1)
print('Series:', str(response))

"""Get Equity Symbol Request"""
response = xt.get_equity_symbol(
    exchangeSegment=1,
    series='EQ',
    symbol='Acc')
print('Equity Symbol:', str(response))

"""Get Expiry Date Request"""
response = xt.get_expiry_date(
    exchangeSegment=2,
    series='FUTIDX',
    symbol='NIFTY')
print('Expiry Date:', str(response))

"""Get Future Symbol Request"""
response = xt.get_future_symbol(
    exchangeSegment=2,
    series='FUTIDX',
    symbol='NIFTY',
    expiryDate='28MAY25JUN')
print('Future Symbol:', str(response))

"""Get Option Symbol Request"""
response = xt.get_option_symbol(
    exchangeSegment=2,
    series='OPTIDX',
    symbol='NIFTY',
    expiryDate='26Mar2020',
    optionType='CE',
    strikePrice=10000)
print('Option Symbol:', str(response))

"""Get Option Type Request"""
response = xt.get_option_type(
    exchangeSegment=2,
    series='OPTIDX',
    symbol='NIFTY',
    expiryDate='26Mar2020')
print('Option Type:', str(response))

"""Get Index List Request"""
response = xt.get_index_list(exchangeSegment=xt.EXCHANGE_NSECM)
print('Index List:', str(response))

"""Search Instrument by ID Request"""
response = xt.search_by_instrumentid(Instruments=instruments)
print('Search By Instrument ID:', str(response))

"""Search Instrument by Scriptname Request"""
response = xt.search_by_scriptname(searchString='REL')
print('Search By Symbol :', str(response))

"""Marketdata Logout Request"""
response = xt.marketdata_logout()
print('Marketdata Logout :', str(response))
