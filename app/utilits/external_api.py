import requests
import json

from app.core.config import API_KEY

def get_list_of_currencies():
    url = 'https://api.apilayer.com/exchangerates_data/symbols'
    headers = {'apikey': API_KEY}

    response = requests.get(url, headers= headers)
    return response.json()
# lst = {\n    \"success\": true,\n    \"symbols\": {\n        \"AED\": \"United Arab Emirates Dirham\",\n        \"AFN\": \"Afghan Afghani\",\n        \"ALL\": \"Albanian Lek\",\n        \"AMD\": \"Armenian Dram\",\n        \"ANG\": \"Netherlands Antillean Guilder\",\n        \"AOA\": \"Angolan Kwanza\",\n        \"ARS\": \"Argentine Peso\",\n        \"AUD\": \"Australian Dollar\",\n        \"AWG\": \"Aruban Florin\",\n        \"AZN\": \"Azerbaijani Manat\",\n        \"BAM\": \"Bosnia-Herzegovina Convertible Mark\",\n        \"BBD\": \"Barbadian Dollar\",\n        \"BDT\": \"Bangladeshi Taka\",\n        \"BGN\": \"Bulgarian Lev\",\n        \"BHD\": \"Bahraini Dinar\",\n        \"BIF\": \"Burundian Franc\",\n        \"BMD\": \"Bermudan Dollar\",\n        \"BND\": \"Brunei Dollar\",\n        \"BOB\": \"Bolivian Boliviano\",\n        \"BRL\": \"Brazilian Real\",\n        \"BSD\": \"Bahamian Dollar\",\n        \"BTC\": \"Bitcoin\",\n        \"BTN\": \"Bhutanese Ngultrum\",\n        \"BWP\": \"Botswanan Pula\",\n        \"BYN\": \"New Belarusian Ruble\",\n        \"BYR\": \"Belarusian Ruble\",\n        \"BZD\": \"Belize Dollar\",\n        \"CAD\": \"Canadian Dollar\",\n        \"CDF\": \"Congolese Franc\",\n        \"CHF\": \"Swiss Franc\",\n        \"CLF\": \"Chilean Unit of Account (UF)\",\n        \"CLP\": \"Chilean Peso\",\n        \"CNY\": \"Chinese Yuan\",\n        \"CNH\": \"Chinese Yuan Offshore\",\n        \"COP\": \"Colombian Peso\",\n        \"CRC\": \"Costa Rican Col\\u00f3n\",\n        \"CUC\": \"Cuban Convertible Peso\",\n        \"CUP\": \"Cuban Peso\",\n        \"CVE\": \"Cape Verdean Escudo\",\n        \"CZK\": \"Czech Republic Koruna\",\n        \"DJF\": \"Djiboutian Franc\",\n        \"DKK\": \"Danish Krone\",\n        \"DOP\": \"Dominican Peso\",\n        \"DZD\": \"Algerian Dinar\",\n        \"EGP\": \"Egyptian Pound\",\n        \"ERN\": \"Eritrean Nakfa\",\n        \"ETB\": \"Ethiopian Birr\",\n        \"EUR\": \"Euro\",\n        \"FJD\": \"Fijian Dollar\",\n        \"FKP\": \"Falkland Islands Pound\",\n        \"GBP\": \"British Pound Sterling\",\n        \"GEL\": \"Georgian Lari\",\n        \"GGP\": \"Guernsey Pound\",\n        \"GHS\": \"Ghanaian Cedi\",\n        \"GIP\": \"Gibraltar Pound\",\n        \"GMD\": \"Gambian Dalasi\",\n        \"GNF\": \"Guinean Franc\",\n        \"GTQ\": \"Guatemalan Quetzal\",\n        \"GYD\": \"Guyanaese Dollar\",\n        \"HKD\": \"Hong Kong Dollar\",\n        \"HNL\": \"Honduran Lempira\",\n        \"HRK\": \"Croatian Kuna\",\n        \"HTG\": \"Haitian Gourde\",\n        \"HUF\": \"Hungarian Forint\",\n        \"IDR\": \"Indonesian Rupiah\",\n        \"ILS\": \"Israeli New Sheqel\",\n        \"IMP\": \"Manx pound\",\n        \"INR\": \"Indian Rupee\",\n        \"IQD\": \"Iraqi Dinar\",\n        \"IRR\": \"Iranian Rial\",\n        \"ISK\": \"Icelandic Kr\\u00f3na\",\n        \"JEP\": \"Jersey Pound\",\n        \"JMD\": \"Jamaican Dollar\",\n        \"JOD\": \"Jordanian Dinar\",\n        \"JPY\": \"Japanese Yen\",\n        \"KES\": \"Kenyan Shilling\",\n        \"KGS\": \"Kyrgystani Som\",\n        \"KHR\": \"Cambodian Riel\",\n        \"KMF\": \"Comorian Franc\",\n        \"KPW\": \"North Korean Won\",\n        \"KRW\": \"South Korean Won\",\n        \"KWD\": \"Kuwaiti Dinar\",\n        \"KYD\": \"Cayman Islands Dollar\",\n        \"KZT\": \"Kazakhstani Tenge\",\n        \"LAK\": \"Laotian Kip\",\n        \"LBP\": \"Lebanese Pound\",\n        \"LKR\": \"Sri Lankan Rupee\",\n        \"LRD\": \"Liberian Dollar\",\n        \"LSL\": \"Lesotho Loti\",\n        \"LTL\": \"Lithuanian Litas\",\n        \"LVL\": \"Latvian Lats\",\n        \"LYD\": \"Libyan Dinar\",\n        \"MAD\": \"Moroccan Dirham\",\n        \"MDL\": \"Moldovan Leu\",\n        \"MGA\": \"Malagasy Ariary\",\n        \"MKD\": \"Macedonian Denar\",\n        \"MMK\": \"Myanma Kyat\",\n        \"MNT\": \"Mongolian Tugrik\",\n        \"MOP\": \"Macanese Pataca\",\n        \"MRU\": \"Mauritanian Ouguiya\",\n        \"MUR\": \"Mauritian Rupee\",\n        \"MVR\": \"Maldivian Rufiyaa\",\n        \"MWK\": \"Malawian Kwacha\",\n        \"MXN\": \"Mexican Peso\",\n        \"MYR\": \"Malaysian Ringgit\",\n        \"MZN\": \"Mozambican Metical\",\n        \"NAD\": \"Namibian Dollar\",\n        \"NGN\": \"Nigerian Naira\",\n        \"NIO\": \"Nicaraguan C\\u00f3rdoba\",\n        \"NOK\": \"Norwegian Krone\",\n        \"NPR\": \"Nepalese Rupee\",\n        \"NZD\": \"New Zealand Dollar\",\n        \"OMR\": \"Omani Rial\",\n        \"PAB\": \"Panamanian Balboa\",\n        \"PEN\": \"Peruvian Nuevo Sol\",\n        \"PGK\": \"Papua New Guinean Kina\",\n        \"PHP\": \"Philippine Peso\",\n        \"PKR\": \"Pakistani Rupee\",\n        \"PLN\": \"Polish Zloty\",\n        \"PYG\": \"Paraguayan Guarani\",\n        \"QAR\": \"Qatari Rial\",\n        \"RON\": \"Romanian Leu\",\n        \"RSD\": \"Serbian Dinar\",\n        \"RUB\": \"Russian Ruble\",\n        \"RWF\": \"Rwandan Franc\",\n        \"SAR\": \"Saudi Riyal\",\n        \"SBD\": \"Solomon Islands Dollar\",\n        \"SCR\": \"Seychellois Rupee\",\n        \"SDG\": \"South Sudanese Pound\",\n        \"SEK\": \"Swedish Krona\",\n        \"SGD\": \"Singapore Dollar\",\n        \"SHP\": \"Saint Helena Pound\",\n        \"SLE\": \"Sierra Leonean Leone\",\n        \"SLL\": \"Sierra Leonean Leone\",\n        \"SOS\": \"Somali Shilling\",\n        \"SRD\": \"Surinamese Dollar\",\n        \"STD\": \"S\\u00e3o Tom\\u00e9 and Pr\\u00edncipe Dobra\",\n        \"SVC\": \"Salvadoran Col\\u00f3n\",\n        \"SYP\": \"Syrian Pound\",\n        \"SZL\": \"Swazi Lilangeni\",\n        \"THB\": \"Thai Baht\",\n        \"TJS\": \"Tajikistani Somoni\",\n        \"TMT\": \"Turkmenistani Manat\",\n        \"TND\": \"Tunisian Dinar\",\n        \"TOP\": \"Tongan Pa\\u02bbanga\",\n        \"TRY\": \"Turkish Lira\",\n        \"TTD\": \"Trinidad and Tobago Dollar\",\n        \"TWD\": \"New Taiwan Dollar\",\n        \"TZS\": \"Tanzanian Shilling\",\n        \"UAH\": \"Ukrainian Hryvnia\",\n        \"UGX\": \"Ugandan Shilling\",\n        \"USD\": \"United States Dollar\",\n        \"UYU\": \"Uruguayan Peso\",\n        \"UZS\": \"Uzbekistan Som\",\n        \"VEF\": \"Venezuelan Bol\\u00edvar Fuerte\",\n        \"VES\": \"Sovereign Bolivar\",\n        \"VND\": \"Vietnamese Dong\",\n        \"VUV\": \"Vanuatu Vatu\",\n        \"WST\": \"Samoan Tala\",\n        \"XAF\": \"CFA Franc BEAC\",\n        \"XAG\": \"Silver (troy ounce)\",\n        \"XAU\": \"Gold (troy ounce)\",\n        \"XCD\": \"East Caribbean Dollar\",\n        \"XDR\": \"Special Drawing Rights\",\n        \"XOF\": \"CFA Franc BCEAO\",\n        \"XPF\": \"CFP Franc\",\n        \"YER\": \"Yemeni Rial\",\n        \"ZAR\": \"South African Rand\",\n        \"ZMK\": \"Zambian Kwacha (pre-2013)\",\n        \"ZMW\": \"Zambian Kwacha\",\n        \"ZWL\": \"Zimbabwean Dollar\"\n    }\n}
def process_list_of_currencies(lst: json):
    codes = lst['symbols']
    return codes



def convert_currencies(_from, to, amount):
    url = f'https://api.apilayer.com/exchangerates_data/convert?to={to}&from={_from}&amount={amount}'

    headers = {'apikey': API_KEY}

    response = requests.get(url, headers= headers)
    return response.json()

def process_convert_currencies(res: json):
    return {'input': res['query'],'result' :res['result'], 'rate': res['info']['rate']}

def get_actual_convert_currencies(base = None, symbols = None):
    if base and symbols:
        url = f'https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}'
    elif base:
        url = f'https://api.apilayer.com/exchangerates_data/latest?base={base}'
    elif symbols:
        url = f'https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}'
    else:
        url = f'https://api.apilayer.com/exchangerates_data/latest'
    
    headers = {'apikey': API_KEY}

    response = requests.get(url, headers= headers)
    return response.json()
