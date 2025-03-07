# pysevdesk
<b>Contact:</b> To contact our support click  <a href='https://landing.sevdesk.de/service-support-center-technik'>here</a><br><br> 
# General information
Welcome to our API!<br>
sevdesk offers you  the possibility of retrieving data using an interface, namely the sevdesk API, and making  changes without having to use the web UI. The sevdesk interface is a REST-Full API. All sevdesk  data and functions that are used in the web UI can also be controlled through the API.

# Cross-Origin Resource Sharing
This API features Cross-Origin Resource Sharing (CORS).<br>
It enables cross-domain communication from the browser.<br>
All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site.

# Embedding resources
When retrieving resources by using this API, you might encounter nested resources in the resources you requested.<br>
For example, an invoice always contains a contact, of which you can see the ID and the object name.<br>
This API gives you the possibility to embed these resources completely into the resources you originally requested.<br>
Taking our invoice example, this would mean, that you would not only see the ID and object name of a contact, but rather the complete contact resource.

To embed resources, all you need to do is to add the query parameter 'embed' to your GET request.<br>
As values, you can provide the name of the nested resource.<br>
Multiple nested resources are also possible by providing multiple names, separated by a comma.
 
# Authentication and Authorization
 The sevdesk API uses a token authentication to authorize calls. For this purpose every sevdesk administrator has one API token, which is a <b>hexadecimal string</b>  containing <b>32 characters</b>. The following clip shows where you can find the  API token if this is your first time with our API.<br><br> <video src='openAPI/img/findingTheApiToken.mp4' controls width='640' height='360'> Your browser cannot play this video.<br> This video explains how to find your sevDesk API token. </video> <br> The token will be needed in every request that you want to send and needs to be provided as a value of an <b>Authorization Header</b>.<br> In this case, we used some random API token. The example shows the token in the Authorization Header. <ul> <li>\"Authorization\" :<span style='color:red'>\"b7794de0085f5cd00560f160f290af38\"</span></li> </ul> The api tokens have an infinite lifetime and, in other words, exist as long as the sevdesk user exists.<br> For this reason, the user should <b>NEVER</b> be deleted.<br> If really necessary, it is advisable to save the api token as we will <b>NOT</b> be able to retrieve it afterwards!<br> It is also possible to generate a new API token, for example, if you want to prevent the usage of your sevdesk account by other people who got your current API token.<br> To achieve this, you just need to click on the \"generate new\" symbol to the right of your token and confirm it with your password. 
# API News
 To never miss API news and updates again, subscribe to our <b>free API newsletter</b> and get all relevant  information to keep your sevdesk software running smoothly. To subscribe, simply click <a href = 'https://landing.sevdesk.de/api-newsletter'><b>here</b></a> and confirm the email address to which we may send all updates relevant to you. 
# API Requests
 In our case, REST API requests need to be build by combining the following components. <table> <tr> <th><b>Component</b></th> <th><b>Description</b></th> </tr> <tr> <td>HTTP-Methods</td> <td> <ul> <li>GET (retrieve a resource)</li> <li>POST (create a resource)</li> <li>PUT (update a resource)</li> <li>DELETE (delete a resource)</li> </ul> </td> </tr> <tr> <td>URL of the API</td> <td><span style='color: #2aa198'>ht</span><span style='color: #2aa198'>tps://my.sevdesk.de/api/v1</span></td> </tr> <tr> <td>URI of the resource</td> <td>The resource to query.<br>For example contacts in sevdesk:<br><br> <span style='color:red'>/Contact</span><br><br> Which will result in the following complete URL:<br><br> <span style='color: #2aa198'>ht</span><span style='color: #2aa198'>tps://my.sevdesk.de/api/v1</span><span style='color:red'>/Contact</span> </td> </tr> <tr> <td>Query parameters</td> <td>Are attached by using the connectives <b>?</b> and <b>&</b> in the URL.<br></td> </tr> <tr> <td>Request headers</td> <td>Typical request headers are for example:<br> <div> <br> <ul> <li>Content-type</li> <li>Authorization</li> <li>Accept-Encoding</li> <li>User-Agent</li> <li>X-Version: Used for resource versioning see information below</li> <li>...</li> </ul> </div> </td> </tr> <tr>  <td>Response headers</td> <td> Typical response headers are for example:<br><br> <div> <ul>  <li>Deprecation: If a resource is deprecated we return true or a timestamp since when</li> <li>...</li> </ul> </div> </td> </tr> <tr> <td>Request body</td> <td>Mostly required in POST and PUT requests.<br> Often the request body contains json, in our case, it also accepts url-encoded data. </td> </tr> </table><br> <span style='color:red'>Note</span>: please pass a meaningful entry at the header \"User-Agent\".  If the \"User-Agent\" is set meaningfully, we can offer better support in case of queries from customers.<br> An example how such a \"User-Agent\" can look like: \"Integration-name by abc\". <br><br> This is a sample request for retrieving existing contacts in sevdesk using curl:<br><br> <img src='openAPI/img/GETRequest.PNG' alt='Get Request' height='150'><br><br> As you can see, the request contains all the components mentioned above.<br> It's HTTP method is GET, it has a correct endpoint  (<span style='color: #2aa198'>ht</span><span style='color: #2aa198'>tps://my.sevdesk.de/api/v1</span><span style='color:red'>/Contact</span>), query parameters and additional <b>header</b> information!<br><br> <b>Query Parameters</b><br><br> As you might have seen in the sample request above, there are several query parameters located in the url.<br> Those are mostly optional but prove to be very useful for a lot of requests as they can limit, extend, sort or filter the data you will get as a response.<br><br> These are the most used query parameter for the sevdesk API. <table> <tr> <th><b>Parameter</b></th> <th><b>Description</b></th> </tr> <tr> <td>embed</td> <td>Will extend some of the returned data.<br> A brief example can be found below.</td> </tr> <tr> <td>countAll</td> <td>\"countAll=true\" returns the number of items</td> </tr> </table> This is an example for the usage of the embed parameter.<br> The following first request will return all company contact entries in sevdesk up to a limit of 100 without any additional information and no offset.<br><br> <img src='openAPI/img/ContactQueryWithoutEmbed.PNG' width='900' height='850'><br><br> Now have a look at the category attribute located in the response.<br> Naturally, it just contains the id and the object name of the object but no further information.<br> We will now use the parameter embed with the value \"category\".<br><br> <img src='openAPI/img/ContactQueryWithEmbed.PNG' width='900' height='850'><br><br> As you can see, the category object is now extended and shows all the attributes and their corresponding values.<br><br> There are lot of other query parameters that can be used to filter the returned data for objects that match a certain pattern, however, those will not be mentioned here and instead can be found at the detail documentation of the most used API endpoints like contact, invoice or voucher.<br><br>
<b>Pagination</b><br> <table> <tr> <th><b>Parameter</b></th> <th><b>Description</b></th> </tr> <tr> <td>limit</td> <td>Limits the number of entries that are returned.<br> Most useful in GET requests which will most likely deliver big sets of data like country or currency lists.<br> In this case, you can bypass the default limitation on returned entries by providing a high number. </td> </tr> <tr> <td>offset</td> <td>Specifies a certain offset for the data that will be returned.<br> As an example, you can specify \"offset=2\" if you want all entries except for the first two.</td> </tr> </table> Example: <ul><li><code>ht<span>tps://my.sevdesk.de/api/v1/Invoice?offset=20&limit=10<span></code></li></ul> <b>Request Headers</b><br><br> The HTTP request (response) headers allow the client as well as the server to pass additional information with the request.<br> They transfer the parameters and arguments which are important for transmitting data over HTTP.<br> Three headers which are useful / necessary when using the sevdesk API are \"Authorization, \"Accept\" and  \"Content-type\".<br> Underneath is a brief description of why and how they should be used.<br><br> <b>Authorization</b><br><br> Should be used to provide your API token in the header. <ul> <li>Authorization:<span style='color:red'>yourApiToken</span></li> </ul> <b>Accept</b><br><br> Specifies the format of the response.<br> Required for operations with a response body. <ul> <li>Accept:application/<span style='color:red'>format</span> </li> </ul> In our case, <code><span style='color:red'>format</span></code> could be replaced with <code>json</code> or <code>xml</code><br><br> <b>Content-type</b><br><br> Specifies which format is used in the request.<br> Is required for operations with a request body. <ul> <li>Content-type:application/<span style='color:red'>format</span></li> </ul> In our case,<code><span style='color:red'>format</span></code>could be replaced with <code>json</code> or <code>x-www-form-urlencoded</code> <br><br><b>API Responses</b><br><br> HTTP status codes<br> When calling the sevdesk API it is very likely that you will get a HTTP status code in the response.<br> Some API calls will also return JSON response bodies which will contain information about the resource.<br> Each status code which is returned will either be a <b>success</b> code or an <b>error</b> code.<br><br> Success codes <table> <tr> <th><b>Status code</b></th> <th><b>Description</b></th> </tr> <tr> <td><code>200 OK</code></td> <td>The request was successful</td> </tr> <tr> <td><code>201 Created</code></td> <td>Most likely to be found in the response of a <b>POST</b> request.<br> This code indicates that the desired resource was successfully created.</td> </tr> </table> <br>Error codes <table> <tr> <th><b>Status code</b></th> <th><b>Description</b></th> </tr> <tr> <td><code>400 Bad request</code></td> <td>The request you sent is most likely syntactically incorrect.<br> You should check if the parameters in the request body or the url are correct.</td> </tr> <tr> <td><code>401 Unauthorized</code></td> <td>The authentication failed.<br> Most likely caused by a missing or wrong API token.</td> </tr> <tr> <td><code>403 Forbidden</code></td> <td>You do not have the permission the access the resource which is requested.</td> </tr> <tr> <td><code>404 Not found</code></td> <td>The resource you specified does not exist.</td> </tr> <tr> <td><code>500 Internal server error</code></td> <td>An internal server error has occurred.<br> Normally this means that something went wrong on our side.<br> However, sometimes this error will appear if we missed to catch an error which is normally a 400 status code! </td> </tr> </table> <br><br> <b>Resource Versioning</b> <br><br> We use resource versioning to handle breaking changes for our endpoints, these are rarely used and will be communicated before we remove older versions.<br> To call a different version we use a specific header <code>X-Version</code> that should be filled with the desired version.<br> <ul>  <li>If you do not specify any version we assume <code>default</code></li> <li>If you specify a version that does not exist or was removed, you will get an error with information which versions are available</li> </ul> <table> <tr> <th>X-Version</th> <th>Description</th> </tr> <tr> <td><code>default</code></td> <td>Should always reference the oldest version.<br> If a specific resource is updated with a new version, <br> then the default version stays the same until the old version is deleted</td> </tr> <tr> <td><code>1.0</code> ... <code>1.9</code></td> <td>Our incrementally version for each resource independent<br> <b>Important</b>: A resource can be available via <code>default</code> but not <code>1.0</code></td> </tr> </table> 
# Your First Request
 After reading the introduction to our API, you should now be able to make your first call.<br> For testing our API, we would always recommend to create a trial account for sevdesk to prevent unwanted changes to your main account.<br> A trial account will be in the highest tariff (materials management), so every sevdesk function can be tested! 

To start testing we would recommend one of the following tools: <ul> <li><a href='https://www.getpostman.com/'>Postman</a></li> <li><a href='https://curl.haxx.se/download.html'>cURL</a></li> </ul> This example will illustrate your first request, which is creating a new Contact in sevdesk.<br> <ol> <li>Download <a href='https://www.getpostman.com/'><b>Postman</b></a> for your desired system and start the application</li> <li>Enter <span><b>ht</span>tps://my.sevdesk.de/api/v1/Contact</b> as the url</li> <li>Create an authorization header and insert your API token as the value</li> <li>For this test, select <b>POST</b> as the HTTP method</li> <li>Go to <b>Headers</b> and enter the key-value pair <b>Content-type</b> + <b>application/x-www-form-urlencoded</b><br> As an alternative, you can just go to <b>Body</b> and select <b>x-www-form-urlencoded</b></li> <li>Now go to <b>Body</b> (if you are not there yet) and enter the key-value pairs as shown in the following picture<br><br> <img src='openAPI/img/FirstRequestPostman.PNG' width='900'><br><br></li> <li>Click on <b>Send</b>. Your response should now look like this:<br><br> <img src='openAPI/img/FirstRequestResponse.PNG' width='900'></li> </ol> As you can see, a successful response in this case returns a JSON-formatted response body containing the contact you just created.<br> For keeping it simple, this was only a minimal example of creating a contact.<br> There are however numerous combinations of parameters that you can provide which add information to your contact. 
# sevdesk-Update 2.0
 Started in 2024 we introduced a new era of bookkeeping in sevdesk. You can check if you already received the update by clicking on your profile in the top right in the sevdesk WebApp or by using the [Tools/bookkeepingSystemVersion endpoint](#tag/Basics/operation/bookkeepingSystemVersion).<br> The old version will be available for some customers until the end of 2024. In this short list we have outlined the changed endpoints with links to jump to the descriptions. If you received the [api newsletter](https://landing.sevdesk.de/api-newsletter) you already know what changed. Otherwise you can check the api changes [here](https://tech.sevdesk.com/api_news/posts/2024_04_04-system-update-breaking-changes/). 
## Check your bookkeeping system version
 With this endpoint you can check which version you / your client uses. On that basis you must use the old or new versions of the endpoints. [Tools/bookkeepingSystemVersion Endpoint](#tag/Basics/operation/bookkeepingSystemVersion) 
## Tax Rules
 <I><b>(affects the properties taxType and taxSet)</b></I><br> With sevdesk-Update 2.0 we changed the available tax rules. Due to a high likeliness of non-compliant accounting, we won't support the following tax type with the sevdesk-Update 2.0 anymore:
 `taxType = custom (this includes 'taxSet': ... )`
 If you only use <code>taxType = default</code>, <code>taxType = eu</code> and / or <code>taxType = ss</code>, these tax types will automatically be mapped to the new tax rules for a transition period, but you have to make sure the taxRate used in positions is within the allowed ones (you may use the [ReceiptGuidance endpoint](#tag/Voucher/operation/forAllAccounts) for that), otherwise the API will return a validation error (HTTP status code 422). For [orders](#tag/Order), [invoices](#tag/Invoice), [vouchers](#tag/Voucher) and [credit notes](#tag/CreditNote) that were created within sevdesk-Update 2.0 the response will change in all endpoints in which these objects are returned.<br> So orders, invoices, vouchers and credit notes created within sevdesk system version 1.0 still have a taxType in the response. When they are created in sevdesk-Update 2.0 they will have a taxRule instead.<br> You can continue to use taxType at first, but we recommend switching to taxRule as there are new options available that were not previously supported.<br> For orders, invoices, vouchers and credit notes that were created within sevdesk-Update 2.0 the response will change in all endpoints in which these objects are returned. This documentation holds the most current version of the endpoints.<br> Here are lists of the currently available tax rules, sorted by their use case, structured into revenue/expense and 'Regelbesteuerer'/'Kleinunternehmer'. 
#### VAT rules for 'Regelbesteuerung' in sevdesk-Update 2.0 (Revenue)
 <table> <tr> <th>VAT Rule</th> <th>New Property</th> <th>Allowed taxRate in positions</th> <th>Old property (deprecated)</th> <th>Unsupported use cases</th> </tr> <tr> <td>Umsatzsteuerpflichtige Umsätze</td> <td><code>'taxRule': 1</code></td> <td> <ul> <li>0.0</li> <li>7.0</li> <li>19.0</li> </ul> </td> <td><code>'taxType': 'default'</code></td> <td>-</td> </tr> <tr> <td>Ausfuhren</td> <td><code>'taxRule': 2</code></td> <td> <ul> <li>0.0</li> </ul> </td> <td>-</td> <td>-</td> </tr> <tr> <td>Innergemeinschaftliche Lieferungen</td> <td><code>'taxRule': 3</code></td> <td> <ul> <li>0.0</li> <li>7.0</li> <li>19.0</li> </ul> </td> <td><code>'taxType': 'eu'</code></td> <td>-</td> </tr> <tr> <td>Steuerfreie Umsätze §4 UStG</td> <td><code>'taxRule': 4</code></td> <td> <ul> <li>0.0</li> </ul> </td> <td>-</td> <td>-</td> </tr> <tr> <td>Reverse Charge gem. §13b UStG</td> <td><code>'taxRule': 5</code></td> <td> <ul> <li>0.0</li> </ul> </td> <td>-</td> <td>-</td> </tr> <tr> <td>Nicht im Inland steuerbare Leistung</td> <td><code>'taxRule': 17</code></td> <td> <ul> <li>0.0</li> </ul> </td> <td><code>'taxType': 'noteu'</code></td> <td> <ul> <li>Creation of an advance invoice</li> <li>Creation of a partial invoice</li> <li>Creation of a final invoice</li> </ul> </td> </tr> <tr> <td>One Stop Shop (goods)</td> <td><code>'taxRule': 18</code></td> <td> <ul> <li>depending on country</li> </ul> </td> <td>-</td> <td> <ul> <li>Usage in vouchers</li> <li>Creation as e-invoice</li> <li>Creation of an invoice with a custom revenue account (<code>accountDatev</code>)</li> <li>Creation of an advance invoice</li> <li>Creation of a partial invoice</li> <li>Creation of a final invoice</li> </ul> </td> </tr> <tr> <td>One Stop Shop (electronic service)</td> <td><code>'taxRule': 19</code></td> <td> <ul> <li>depending on country</li> </ul> </td> <td>-</td> <td> <ul> <li>Usage in vouchers</li> <li>Creation as e-invoice</li> <li>Creation of an invoice with a custom revenue account (<code>accountDatev</code>)</li> <li>Creation of an advance invoice</li> <li>Creation of a partial invoice</li> <li>Creation of a final invoice</li> </ul> </td> </tr> <tr> <td>One Stop Shop (other service)</td> <td><code>'taxRule': 20</code></td> <td> <ul> <li>depending on country</li> </ul> </td> <td>-</td> <td> <ul> <li>Usage in vouchers</li> <li>Creation as e-invoice</li> <li>Creation of an invoice with a custom revenue account (<code>accountDatev</code>)</li> <li>Creation of an advance invoice</li> <li>Creation of a partial invoice</li> <li>Creation of a final invoice</li> </ul> </td> </tr> </table> 
 See the <a href=\"#tag/Invoice/operation/createInvoiceFromOrder\">example request</a> to create a normal invoice <code>\"invoiceType\": \"RE\"</code> from an order that uses a tax rule that does not support advance, partial or final invoices. 
 
#### VAT rules for 'Regelbesteuerung' in sevdesk-Update 2.0 (Expense)
 <table> <tr> <th>VAT Rule</th> <th>New Property</th> <th>Allowed taxRate in positions</th> <th>Old property (deprecated)</th> </tr> <tr> <td>Innergemeinschaftliche Erwerbe</td> <td><code>'taxRule': 8</code></td> <td> <ul> <li>0.0</li> <li>7.0</li> <li>19.0</li> </ul> </td> <td>-</td> </tr> <tr> <td>Vorsteuerabziehbare Aufwendungen</td> <td><code>'taxRule': 9</code></td> <td> <ul> <li>0.0</li> <li>7.0</li> <li>19.0</li> </ul> </td> <td><code>'taxType': 'default'</code></td> </tr> <tr> <td>Nicht vorsteuerabziehbare Aufwendungen</td> <td><code>'taxRule': 10</code></td> <td> <ul> <li>0.0</li> </ul> </td> <td>-</td> </tr> <tr> <td>Reverse Charge gem. §13b Abs. 2 UStG mit Vorsteuerabzug 0% (19%)</td> <td><code>'taxRule': 12</code></td> <td> <ul> <li>0.0</li> </ul> </td> <td>-</td> </tr> <tr> <td>Reverse Charge gem. §13b UStG ohne Vorsteuerabzug 0% (19%)</td> <td><code>'taxRule': 13</code></td> <td> <ul> <li>0.0</li> </ul> </td> <td>-</td> </tr> <tr> <td>Reverse Charge gem. §13b Abs. 1 EU Umsätze 0% (19%)</td> <td><code>'taxRule': 14</code></td> <td> <ul> <li>0.0</li> </ul> </td> <td>-</td> </tr> </table> 
 
#### VAT rules for small business owner ('Kleinunternehmer') in sevdesk-Update 2.0 (Revenue)
 <table> <tr> <th>VAT Rule</th> <th>New Property</th> <th>Allowed taxRate in positions</th> <th>Old property (deprecated)</th> </tr> <tr> <td>Steuer nicht erhoben nach §19UStG</td> <td><code>'taxRule': 11</code></td> <td> <ul> <li>0.0</li> </ul> </td> <td><code>'taxType': 'ss'</code></td> </tr> </table> 
 
#### VAT rules for small business owner ('Kleinunternehmer') in sevdesk-Update 2.0 (Expense)
 <table> <tr> <th>VAT Rule</th> <th>New Property</th> <th>Allowed taxRate in positions</th> <th>Old property (deprecated)</th> </tr> <tr> <td>Nicht vorsteuerabziehbare Aufwendungen</td> <td><code>'taxRule': 10</code></td> <td> <ul> <li>0.0</li> </ul> </td> <td><code>'taxType': 'ss'</code></td> </tr> <tr> <td>Reverse Charge gem. §13b UStG ohne Vorsteuerabzug 0% (19%)</td> <td><code>'taxRule': 13</code></td> <td> <ul> <li>0.0</li> </ul> </td> <td>-</td> </tr> </table> 
 
## Booking Accounts
 <I><b>(affects the property accountingType)</b></I><br> With sevdesk-Update 2.0 we changed the available booking accounts and their combinatorics. If you use accountingTypes with SKR numbers that are still available in our receipt guidance, you do not have to change anything in your requests. These booking accounts will automatically be mapped to the new representation (Account Datev). But you have to make sure the taxRate used in positions and taxRule used in the voucher is within the allowed ones (check the [ReceiptGuidance](#tag/Voucher/operation/forAllAccounts)) of the provided booking account, otherwise the API will return a validation error (HTTP status code 422). For orders, invoices, vouchers and credit notes in that were created within sevdesk-Update 2.0 the response will change in all endpoints were these objects are returned. 
## Receipt Guidance
 To help you decide which account can be used in conjunction with which tax rules, tax rates and documents, we created several guidance endpoints just there for you to get helpful information. You can find the descriptions in the changes section for Vouchers below or jump directly to the endpoint description by using this link: [Receipt Guidance](#tag/Voucher/operation/forAllAccounts).<br> Receipt Guidance is planned to give you guidance in which account you can pick (depending on your filter criteria and the client settings (e.g. 'Kleinunternehmer')) and which tax rate and [tax rules](#section/sevdesk-Update-2.0/Tax-Rules) are comptaible with them.  
## Vouchers
 
### Saving a new voucher ([Voucher/Factory/saveVoucher](#tag/Voucher/operation/voucherFactorySaveVoucher))
 Following use cases do not work anymore or have changed: <ol> <li>Custom vat regulations (taxType = custom and provided taxSet)</li> <li>Only specific tax rates and booking accounts are available. Check [ReceiptGuidance](#tag/Voucher/operation/forAllAccounts)</li> <li>Custom accounting types do not work anymore</li> <li>Using an asset booking account without creating an asset is no longer possible</li> <li>A voucher can not be directly set to paid anymore, therefore only status <code>DRAFT (50)</code> or <code>UNPAID / DUE (100)</code> are possible when creating a new voucher. Use the [/api/v1/Voucher/{voucherId}/bookAmount endpoint](#tag/Voucher/operation/bookVoucher) to set a voucher to paid</li> <li>Setting or changing the property enshrined. Use our new endpoint [/api/v1/Voucher/{voucherId}/enshrine](#tag/Voucher/operation/voucherEnshrine) to enshrine a voucher</li> </ol> 
### Get or update an existing voucher ([Voucher/{voucherId}](#tag/Voucher/operation/updateVoucher))
 Following use cases do not work anymore or have changed: <ol> <li>Custom vat regulations (taxType = custom and provided taxSet)</li> <li>See [ReceiptGuidance](#tag/Voucher/operation/forAllAccounts) to check which tax rates are available in conjunction with which tax rules</li> </ol> 
### Book a voucher ([Voucher/{voucherId}](#tag/Voucher/operation/bookVoucher))
 Following use cases do not work anymore or have changed: <ol> <li>Voucher with negative voucher positions can not use 'cash discount' as a payment difference anymore</li> <li>A Voucher can only be booked when it was registered beforehand (see above)</li> <li>Based on the combination of voucher positions some payment difference reasons are not possible anymore</li> <li>The currency fluctuation (CF) type is no longer supported as a payment difference reason</li> </ol> 
## Banking
 Following use cases do not work anymore or have changed: <ol> <li>Setting or changing the property enshrined will now only be available by using the [appropriate enshrine endpoint](#tag/CheckAccountTransaction/operation/checkAccountTransactionEnshrine)</li> </ol> 
## Invoicing
 The changes to the vat rules also apply here. Check the documentation of voucher above as the changes are the same. 
### General stricter validation in PUT and POST endpoints
 We added stricter validation to ensure only correct invoices are created which than can be further processed in sevdesk. Following use cases do not work anymore or have changed: <ol> <li>Creating an invoice with taxType <code>custom</code> does not work anymore</li> <li>Processing an invoice beyond status <code>DRAFT (100)</code> without a contact does not work anymore</li> <li>Advanced invoices (<code>invoiceType: 'AR'</code>) and partial invoices (<code>invoiceType: 'TR'</code>) can only be created with the tax rule 'Umsatzsteuerpflichtige Umsätze (taxRule: 1)'(for Regelbesteuerer) or 'Steuer nicht erhoben nach §19 UStG (taxRule: 11)'(for Kleinunternehmer)</li> <li>Creating a dunning (<code>invoiceType: 'MA'</code>) with the value of property <code>reminderCharge</code> greater than 0 does not work anymore</li> <li>Creating an advanced invoice (<code>invoiceType: 'AR'</code>), a partial invoice (<code>invoiceType: 'TR'</code>) or a final invoice (<code>invoiceType: 'ER'</code>) with a currency deviating from the clients <code>defaultCurrency</code> is not possible anymore</li> <li>Changing the status manually does not work anymore (see 'Removed endpoint /Invoice/{invoiceId}/changeStatus' below)</li> <li>Enshrining now has to be done by using the [enshrine endpoint](#tag/Invoice/operation/invoiceEnshrine) (see below)</li> </ol> 
### Saving an invoice ([Invoice/Factory/saveInvoice](#tag/Invoice/operation/createInvoiceByFactory))
 Following use cases do not work anymore or have changed: <ol> <li>Invoices can only be created with the status <code>DRAFT (100)</code> and can not be changed manually. Use the matching endpoints (e.g. [sendViaEmail](#tag/Invoice/operation/sendInvoiceViaEMail)) to automatically change the status accordingly</li> <li>Setting or changing the property <code>enshrined</code> is now only possible by using the [enshrine endpoint](#tag/CheckAccountTransaction/operation/checkAccountTransactionEnshrine)</li> </ol> 
### Using an order to create an invoice ([Invoice/Factory/createInvoiceFromOrder](#tag/Invoice/operation/createInvoiceFromOrder))
 Following use cases do not work anymore or have changed: <ol> <li>Creating a final invoice (partialType: 'ER') is not possible if an advanced invoice (partialType: 'AR') or partial invoice (partialType: 'TR') exists. This functionality will be added in a later update</li> </ol> 
### Removed endpoint /Invoice/{invoiceId}/changeStatus
 This endpoint will be completely removed (including sevdesk system version 1.0!). Using these endpoints will automatically change the status accordingly: <ul> <li>[Invoice/{invoiceId}/sendViaEmail](#tag/Invoice/operation/sendInvoiceViaEMail)</li> <li>[Invoice/{invoiceId}/sendBy](#tag/Invoice/operation/invoiceSendBy)</li> <li>[Invoice/{invoiceId}/bookAmount](#tag/Invoice/operation/bookInvoice)</li> <li>[Invoice/{invoiceId}/resetToDraft](#tag/Invoice/operation/invoiceResetToDraft)</li> <li>[Invoice/{invoiceId}/resetToOpen](#tag/Invoice/operation/invoiceResetToOpen)</li> </ul> 
### New endpoint [Invoice/{invoiceId}/resetToDraft](#tag/Invoice/operation/invoiceResetToDraft)
 This new endpoint can be used to reset the status of an invoice to <code>DRAFT (100)</code>. 
### New endpoint [Invoice/{invoiceId}/resetToOpen](#tag/Invoice/operation/invoiceResetToOpen)
 This new endpoint can be used to reset the status of an invoice to <code>OPEN (200)</code>. 
### New endpoint [Invoice/{invoiceId}/enshrine]((#tag/Invoice/operation/invoiceEnshrine))
 The enshrine endpoint is now used to set the property <code>enshrined</code>. <b>This operation CAN NOT be undone due to legal reasons!</b> 
## Credit Notes
 The changes to the vat rules also apply here. Check the documentation of voucher above as the changes are the same. 
### General stricter validation in PUT and POST endpoints
 We added stricter validation to ensure only correct credit notes are created which than can be further processed in sevdesk. Due to the move from taxTypes/taxSets to taxRules you need to check the compatibility of the taxRules in combination with the tax rates. Following use cases do not work anymore or have changed: <ol> <li>Creating a credit note without a date of delivery (<code>deliveryDateUntil</code>) for an invoice that has a date of delivery (<code>deliveryDateUntil</code>) is no longer possible</li> <li>Creating a credit note with a date of delivery (<code>deliveryDateUntil</code>) for an invoice that has no date of delivery (<code>deliveryDateUntil</code>) is no longer possible</li> <li>Creating a credit note with a date of delivery (<code>deliveryDateUntil</code>) that is before the date of delivery (<code>deliveryDateUntil</code>) of the invoice is no longer possible</li> <li>Creating a credit note for an advanced invoice (<code>invoiceType: 'AR'</code>) or partial invoice (<code>invoiceType: 'TR'</code>) is no longer possible</li> <li>Creating a credit note for a voucher is no longer possible</li> <li>Creating a credit note with a <code>bookingCategory</code> other than <code>UNDERACHIEVEMENT</code> is no longer possible</li> <li>Currency fluctuation (CF) is no longer supported as a payment difference</li> </ol> 
### Saving a credit note ([CreditNote/Factory/saveCreditNote](#tag/CreditNote/operation/createcreditNote))
 Following use cases do not work anymore or have changed: <ol> <li>Credit notes can only be created with the status <code>DRAFT (100)</code> and can not be changed manually. Use the matching endpoints (e.g. [sendViaEmail](#tag/CreditNote/operation/sendCreditNoteViaEMail)) to automatically change the status accordingly</li> <li>Enshrining now has to be done by using the enshrine endpoint (see below)</li> </ol> 
### Removed endpoint /CreditNote/Factory/createFromVoucher
 The endpoint will be removed. It is not possible anymore to create credit notes for vouchers within sevdesk-Update 2.0. The endpoint continues to stay available for existing sevdesk system version 1.0 clients. 
### Removed endpoint /CreditNote/{creditNoteId}/changeStatus
 This endpoint will be completely removed (including sevdesk system version 1.0!). Using these endpoints will automatically change the status accordingly: <ul> <li>[CreditNote/{creditNoteId}/sendViaEmail](#tag/CreditNote/operation/sendCreditNoteViaEMail)</li> <li>[CreditNote/{creditNoteId}/sendBy](#tag/CreditNote/operation/creditNoteSendBy)</li> <li>[CreditNote/{creditNoteId}/bookAmount](#tag/CreditNote/operation/bookCreditNote)</li> <li>[CreditNote/{creditNoteId}/resetToDraft](#tag/CreditNote/operation/creditNoteResetToDraft)</li> <li>[CreditNote/{creditNoteId}/resetToOpen](#tag/CreditNote/operation/creditNoteResetToOpen)</li> </ul> 
### New endpoint CreditNote/{creditNoteId}/resetToDraft
 This new endpoint can be used to reset the status of a credit note to <code>DRAFT (100)</code>. You can find the documentation [here](#tag/CreditNote/operation/creditNoteResetToDraft). 
### New endpoint CreditNote/{creditNoteId}/resetToOpen
 This new endpoint can be used to reset the status of a credit note to <code>OPEN (200)</code>. You can find the documentation [here](#tag/CreditNote/operation/creditNoteResetToOpen). 
### New endpoint CreditNote/{creditNoteId}/enshrine
 [The enshrine endpoint](#tag/CreditNote/operation/creditNoteEnshrine) is now used to set the property <code>enshrined</code>. <b>This operation CAN NOT be undone due to legal reasons!</b>
## Parts
 
### General stricter validation in PUT and POST endpoints
 Following use cases do not work anymore or have changed: <ol> <li>Creating products with a tax rate other than 0.0, 7.0 and 19.0 is no longer possible</li> </ol> 

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.0
- Package version: 0.1.0
- Generator version: 7.11.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import pysevdesk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pysevdesk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import pysevdesk
from pysevdesk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.sevdesk.de/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pysevdesk.Configuration(
    host = "https://my.sevdesk.de/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'


# Enter a context with an instance of the API client
with pysevdesk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pysevdesk.AccountingContactApi(api_client)
    model_accounting_contact = pysevdesk.ModelAccountingContact() # ModelAccountingContact | Creation data (optional)

    try:
        # Create a new accounting contact
        api_response = api_instance.create_accounting_contact(model_accounting_contact=model_accounting_contact)
        print("The response of AccountingContactApi->create_accounting_contact:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountingContactApi->create_accounting_contact: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://my.sevdesk.de/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountingContactApi* | [**create_accounting_contact**](docs/AccountingContactApi.md#create_accounting_contact) | **POST** /AccountingContact | Create a new accounting contact
*AccountingContactApi* | [**delete_accounting_contact**](docs/AccountingContactApi.md#delete_accounting_contact) | **DELETE** /AccountingContact/{accountingContactId} | Deletes an accounting contact
*AccountingContactApi* | [**get_accounting_contact**](docs/AccountingContactApi.md#get_accounting_contact) | **GET** /AccountingContact | Retrieve accounting contact
*AccountingContactApi* | [**get_accounting_contact_by_id**](docs/AccountingContactApi.md#get_accounting_contact_by_id) | **GET** /AccountingContact/{accountingContactId} | Find accounting contact by ID
*AccountingContactApi* | [**update_accounting_contact**](docs/AccountingContactApi.md#update_accounting_contact) | **PUT** /AccountingContact/{accountingContactId} | Update an existing accounting contact
*BasicsApi* | [**bookkeeping_system_version**](docs/BasicsApi.md#bookkeeping_system_version) | **GET** /Tools/bookkeepingSystemVersion | Retrieve bookkeeping system version
*CheckAccountApi* | [**create_clearing_account**](docs/CheckAccountApi.md#create_clearing_account) | **POST** /CheckAccount/Factory/clearingAccount | Create a new clearing account
*CheckAccountApi* | [**create_file_import_account**](docs/CheckAccountApi.md#create_file_import_account) | **POST** /CheckAccount/Factory/fileImportAccount | Create a new file import account
*CheckAccountApi* | [**delete_check_account**](docs/CheckAccountApi.md#delete_check_account) | **DELETE** /CheckAccount/{checkAccountId} | Deletes a check account
*CheckAccountApi* | [**get_balance_at_date**](docs/CheckAccountApi.md#get_balance_at_date) | **GET** /CheckAccount/{checkAccountId}/getBalanceAtDate | Get the balance at a given date
*CheckAccountApi* | [**get_check_account_by_id**](docs/CheckAccountApi.md#get_check_account_by_id) | **GET** /CheckAccount/{checkAccountId} | Find check account by ID
*CheckAccountApi* | [**get_check_accounts**](docs/CheckAccountApi.md#get_check_accounts) | **GET** /CheckAccount | Retrieve check accounts
*CheckAccountApi* | [**update_check_account**](docs/CheckAccountApi.md#update_check_account) | **PUT** /CheckAccount/{checkAccountId} | Update an existing check account
*CheckAccountTransactionApi* | [**check_account_transaction_enshrine**](docs/CheckAccountTransactionApi.md#check_account_transaction_enshrine) | **PUT** /CheckAccountTransaction/{checkAccountTransactionId}/enshrine | Enshrine
*CheckAccountTransactionApi* | [**create_transaction**](docs/CheckAccountTransactionApi.md#create_transaction) | **POST** /CheckAccountTransaction | Create a new transaction
*CheckAccountTransactionApi* | [**delete_check_account_transaction**](docs/CheckAccountTransactionApi.md#delete_check_account_transaction) | **DELETE** /CheckAccountTransaction/{checkAccountTransactionId} | Deletes a check account transaction
*CheckAccountTransactionApi* | [**get_check_account_transaction_by_id**](docs/CheckAccountTransactionApi.md#get_check_account_transaction_by_id) | **GET** /CheckAccountTransaction/{checkAccountTransactionId} | Find check account transaction by ID
*CheckAccountTransactionApi* | [**get_transactions**](docs/CheckAccountTransactionApi.md#get_transactions) | **GET** /CheckAccountTransaction | Retrieve transactions
*CheckAccountTransactionApi* | [**update_check_account_transaction**](docs/CheckAccountTransactionApi.md#update_check_account_transaction) | **PUT** /CheckAccountTransaction/{checkAccountTransactionId} | Update an existing check account transaction
*CommunicationWayApi* | [**create_communication_way**](docs/CommunicationWayApi.md#create_communication_way) | **POST** /CommunicationWay | Create a new contact communication way
*CommunicationWayApi* | [**delete_communication_way**](docs/CommunicationWayApi.md#delete_communication_way) | **DELETE** /CommunicationWay/{communicationWayId} | Deletes a communication way
*CommunicationWayApi* | [**get_communication_way_by_id**](docs/CommunicationWayApi.md#get_communication_way_by_id) | **GET** /CommunicationWay/{communicationWayId} | Find communication way by ID
*CommunicationWayApi* | [**get_communication_way_keys**](docs/CommunicationWayApi.md#get_communication_way_keys) | **GET** /CommunicationWayKey | Retrieve communication way keys
*CommunicationWayApi* | [**get_communication_ways**](docs/CommunicationWayApi.md#get_communication_ways) | **GET** /CommunicationWay | Retrieve communication ways
*CommunicationWayApi* | [**update_communication_way**](docs/CommunicationWayApi.md#update_communication_way) | **PUT** /CommunicationWay/{communicationWayId} | Update a existing communication way
*ContactApi* | [**contact_customer_number_availability_check**](docs/ContactApi.md#contact_customer_number_availability_check) | **GET** /Contact/Mapper/checkCustomerNumberAvailability | Check if a customer number is available
*ContactApi* | [**create_contact**](docs/ContactApi.md#create_contact) | **POST** /Contact | Create a new contact
*ContactApi* | [**delete_contact**](docs/ContactApi.md#delete_contact) | **DELETE** /Contact/{contactId} | Deletes a contact
*ContactApi* | [**find_contacts_by_custom_field_value**](docs/ContactApi.md#find_contacts_by_custom_field_value) | **GET** /Contact/Factory/findContactsByCustomFieldValue | Find contacts by custom field value
*ContactApi* | [**get_contact_by_id**](docs/ContactApi.md#get_contact_by_id) | **GET** /Contact/{contactId} | Find contact by ID
*ContactApi* | [**get_contact_tabs_item_count_by_id**](docs/ContactApi.md#get_contact_tabs_item_count_by_id) | **GET** /Contact/{contactId}/getTabsItemCount | Get number of all items
*ContactApi* | [**get_contacts**](docs/ContactApi.md#get_contacts) | **GET** /Contact | Retrieve contacts
*ContactApi* | [**get_next_customer_number**](docs/ContactApi.md#get_next_customer_number) | **GET** /Contact/Factory/getNextCustomerNumber | Get next free customer number
*ContactApi* | [**update_contact**](docs/ContactApi.md#update_contact) | **PUT** /Contact/{contactId} | Update a existing contact
*ContactAddressApi* | [**contact_address_id**](docs/ContactAddressApi.md#contact_address_id) | **GET** /ContactAddress/{contactAddressId} | Find contact address by ID
*ContactAddressApi* | [**create_contact_address**](docs/ContactAddressApi.md#create_contact_address) | **POST** /ContactAddress | Create a new contact address
*ContactAddressApi* | [**delete_contact_address**](docs/ContactAddressApi.md#delete_contact_address) | **DELETE** /ContactAddress/{contactAddressId} | Deletes a contact address
*ContactAddressApi* | [**get_contact_addresses**](docs/ContactAddressApi.md#get_contact_addresses) | **GET** /ContactAddress | Retrieve contact addresses
*ContactAddressApi* | [**update_contact_address**](docs/ContactAddressApi.md#update_contact_address) | **PUT** /ContactAddress/{contactAddressId} | update a existing contact address
*ContactFieldApi* | [**create_contact_field**](docs/ContactFieldApi.md#create_contact_field) | **POST** /ContactCustomField | Create contact field
*ContactFieldApi* | [**create_contact_field_setting**](docs/ContactFieldApi.md#create_contact_field_setting) | **POST** /ContactCustomFieldSetting | Create contact field setting
*ContactFieldApi* | [**delete_contact_custom_field_id**](docs/ContactFieldApi.md#delete_contact_custom_field_id) | **DELETE** /ContactCustomField/{contactCustomFieldId} | delete a contact field
*ContactFieldApi* | [**delete_contact_field_setting**](docs/ContactFieldApi.md#delete_contact_field_setting) | **DELETE** /ContactCustomFieldSetting/{contactCustomFieldSettingId} | Deletes a contact field setting
*ContactFieldApi* | [**get_contact_field_setting_by_id**](docs/ContactFieldApi.md#get_contact_field_setting_by_id) | **GET** /ContactCustomFieldSetting/{contactCustomFieldSettingId} | Find contact field setting by ID
*ContactFieldApi* | [**get_contact_field_settings**](docs/ContactFieldApi.md#get_contact_field_settings) | **GET** /ContactCustomFieldSetting | Retrieve contact field settings
*ContactFieldApi* | [**get_contact_fields**](docs/ContactFieldApi.md#get_contact_fields) | **GET** /ContactCustomField | Retrieve contact fields
*ContactFieldApi* | [**get_contact_fields_by_id**](docs/ContactFieldApi.md#get_contact_fields_by_id) | **GET** /ContactCustomField/{contactCustomFieldId} | Retrieve contact fields
*ContactFieldApi* | [**get_placeholder**](docs/ContactFieldApi.md#get_placeholder) | **GET** /Textparser/fetchDictionaryEntriesByType | Retrieve Placeholders
*ContactFieldApi* | [**get_reference_count**](docs/ContactFieldApi.md#get_reference_count) | **GET** /ContactCustomFieldSetting/{contactCustomFieldSettingId}/getReferenceCount | Receive count reference
*ContactFieldApi* | [**update_contact_field_setting**](docs/ContactFieldApi.md#update_contact_field_setting) | **PUT** /ContactCustomFieldSetting/{contactCustomFieldSettingId} | Update contact field setting
*ContactFieldApi* | [**update_contactfield**](docs/ContactFieldApi.md#update_contactfield) | **PUT** /ContactCustomField/{contactCustomFieldId} | Update a contact field
*CreditNoteApi* | [**book_credit_note**](docs/CreditNoteApi.md#book_credit_note) | **PUT** /CreditNote/{creditNoteId}/bookAmount | Book a credit note
*CreditNoteApi* | [**create_credit_note_from_invoice**](docs/CreditNoteApi.md#create_credit_note_from_invoice) | **POST** /CreditNote/Factory/createFromInvoice | Creates a new creditNote from an invoice
*CreditNoteApi* | [**create_credit_note_from_voucher**](docs/CreditNoteApi.md#create_credit_note_from_voucher) | **POST** /CreditNote/Factory/createFromVoucher | Creates a new creditNote from a voucher
*CreditNoteApi* | [**createcredit_note**](docs/CreditNoteApi.md#createcredit_note) | **POST** /CreditNote/Factory/saveCreditNote | Create a new creditNote
*CreditNoteApi* | [**credit_note_enshrine**](docs/CreditNoteApi.md#credit_note_enshrine) | **PUT** /CreditNote/{creditNoteId}/enshrine | Enshrine
*CreditNoteApi* | [**credit_note_get_pdf**](docs/CreditNoteApi.md#credit_note_get_pdf) | **GET** /CreditNote/{creditNoteId}/getPdf | Retrieve pdf document of a credit note
*CreditNoteApi* | [**credit_note_reset_to_draft**](docs/CreditNoteApi.md#credit_note_reset_to_draft) | **PUT** /CreditNote/{creditNoteId}/resetToDraft | Reset status to draft
*CreditNoteApi* | [**credit_note_reset_to_open**](docs/CreditNoteApi.md#credit_note_reset_to_open) | **PUT** /CreditNote/{creditNoteId}/resetToOpen | Reset status to open
*CreditNoteApi* | [**credit_note_send_by**](docs/CreditNoteApi.md#credit_note_send_by) | **PUT** /CreditNote/{creditNoteId}/sendBy | Mark credit note as sent
*CreditNoteApi* | [**deletecredit_note**](docs/CreditNoteApi.md#deletecredit_note) | **DELETE** /CreditNote/{creditNoteId} | Deletes an creditNote
*CreditNoteApi* | [**get_credit_notes**](docs/CreditNoteApi.md#get_credit_notes) | **GET** /CreditNote | Retrieve CreditNote
*CreditNoteApi* | [**getcredit_note_by_id**](docs/CreditNoteApi.md#getcredit_note_by_id) | **GET** /CreditNote/{creditNoteId} | Find creditNote by ID
*CreditNoteApi* | [**send_credit_note_by_printing**](docs/CreditNoteApi.md#send_credit_note_by_printing) | **GET** /CreditNote/{creditNoteId}/sendByWithRender | Send credit note by printing
*CreditNoteApi* | [**send_credit_note_via_e_mail**](docs/CreditNoteApi.md#send_credit_note_via_e_mail) | **POST** /CreditNote/{creditNoteId}/sendViaEmail | Send credit note via email
*CreditNoteApi* | [**updatecredit_note**](docs/CreditNoteApi.md#updatecredit_note) | **PUT** /CreditNote/{creditNoteId} | Update an existing creditNote
*CreditNotePosApi* | [**getcredit_note_positions**](docs/CreditNotePosApi.md#getcredit_note_positions) | **GET** /CreditNotePos | Retrieve creditNote positions
*ExportApi* | [**export_contact**](docs/ExportApi.md#export_contact) | **GET** /Export/contactListCsv | Export contact
*ExportApi* | [**export_credit_note**](docs/ExportApi.md#export_credit_note) | **GET** /Export/creditNoteCsv | Export creditNote
*ExportApi* | [**export_datev**](docs/ExportApi.md#export_datev) | **GET** /Export/datevCSV | Export datev
*ExportApi* | [**export_invoice**](docs/ExportApi.md#export_invoice) | **GET** /Export/invoiceCsv | Export invoice
*ExportApi* | [**export_invoice_zip**](docs/ExportApi.md#export_invoice_zip) | **GET** /Export/invoiceZip | Export Invoice as zip
*ExportApi* | [**export_transactions**](docs/ExportApi.md#export_transactions) | **GET** /Export/transactionsCsv | Export transaction
*ExportApi* | [**export_voucher**](docs/ExportApi.md#export_voucher) | **GET** /Export/voucherListCsv | Export voucher as zip
*ExportApi* | [**export_voucher_zip**](docs/ExportApi.md#export_voucher_zip) | **GET** /Export/voucherZip | Export voucher zip
*ExportApi* | [**update_export_config**](docs/ExportApi.md#update_export_config) | **PUT** /SevClient/{SevClientId}/updateExportConfig | Update export config
*InvoiceApi* | [**book_invoice**](docs/InvoiceApi.md#book_invoice) | **PUT** /Invoice/{invoiceId}/bookAmount | Book an invoice
*InvoiceApi* | [**cancel_invoice**](docs/InvoiceApi.md#cancel_invoice) | **POST** /Invoice/{invoiceId}/cancelInvoice | Cancel an invoice / Create cancellation invoice
*InvoiceApi* | [**create_invoice_by_factory**](docs/InvoiceApi.md#create_invoice_by_factory) | **POST** /Invoice/Factory/saveInvoice | Create a new invoice
*InvoiceApi* | [**create_invoice_from_order**](docs/InvoiceApi.md#create_invoice_from_order) | **POST** /Invoice/Factory/createInvoiceFromOrder | Create invoice from order
*InvoiceApi* | [**create_invoice_reminder**](docs/InvoiceApi.md#create_invoice_reminder) | **POST** /Invoice/Factory/createInvoiceReminder | Create invoice reminder
*InvoiceApi* | [**get_invoice_by_id**](docs/InvoiceApi.md#get_invoice_by_id) | **GET** /Invoice/{invoiceId} | Find invoice by ID
*InvoiceApi* | [**get_invoice_positions_by_id**](docs/InvoiceApi.md#get_invoice_positions_by_id) | **GET** /Invoice/{invoiceId}/getPositions | Find invoice positions
*InvoiceApi* | [**get_invoices**](docs/InvoiceApi.md#get_invoices) | **GET** /Invoice | Retrieve invoices
*InvoiceApi* | [**get_is_invoice_partially_paid**](docs/InvoiceApi.md#get_is_invoice_partially_paid) | **GET** /Invoice/{invoiceId}/getIsPartiallyPaid | Check if an invoice is already partially paid
*InvoiceApi* | [**invoice_enshrine**](docs/InvoiceApi.md#invoice_enshrine) | **PUT** /Invoice/{invoiceId}/enshrine | Enshrine
*InvoiceApi* | [**invoice_get_pdf**](docs/InvoiceApi.md#invoice_get_pdf) | **GET** /Invoice/{invoiceId}/getPdf | Retrieve pdf document of an invoice
*InvoiceApi* | [**invoice_get_xml**](docs/InvoiceApi.md#invoice_get_xml) | **GET** /Invoice/{invoiceId}/getXml | Retrieve XML of an e-invoice
*InvoiceApi* | [**invoice_render**](docs/InvoiceApi.md#invoice_render) | **POST** /Invoice/{invoiceId}/render | Render the pdf document of an invoice
*InvoiceApi* | [**invoice_reset_to_draft**](docs/InvoiceApi.md#invoice_reset_to_draft) | **PUT** /Invoice/{invoiceId}/resetToDraft | Reset status to draft
*InvoiceApi* | [**invoice_reset_to_open**](docs/InvoiceApi.md#invoice_reset_to_open) | **PUT** /Invoice/{invoiceId}/resetToOpen | Reset status to open
*InvoiceApi* | [**invoice_send_by**](docs/InvoiceApi.md#invoice_send_by) | **PUT** /Invoice/{invoiceId}/sendBy | Mark invoice as sent
*InvoiceApi* | [**send_invoice_via_e_mail**](docs/InvoiceApi.md#send_invoice_via_e_mail) | **POST** /Invoice/{invoiceId}/sendViaEmail | Send invoice via email
*InvoicePosApi* | [**get_invoice_pos**](docs/InvoicePosApi.md#get_invoice_pos) | **GET** /InvoicePos | Retrieve InvoicePos
*LayoutApi* | [**get_letterpapers_with_thumb**](docs/LayoutApi.md#get_letterpapers_with_thumb) | **GET** /DocServer/getLetterpapersWithThumb | Retrieve letterpapers
*LayoutApi* | [**get_templates**](docs/LayoutApi.md#get_templates) | **GET** /DocServer/getTemplatesWithThumb | Retrieve templates
*LayoutApi* | [**update_credit_note_template**](docs/LayoutApi.md#update_credit_note_template) | **PUT** /CreditNote/{creditNoteId}/changeParameter | Update an of credit note template
*LayoutApi* | [**update_invoice_template**](docs/LayoutApi.md#update_invoice_template) | **PUT** /Invoice/{invoiceId}/changeParameter | Update an invoice template
*LayoutApi* | [**update_order_template**](docs/LayoutApi.md#update_order_template) | **PUT** /Order/{orderId}/changeParameter | Update an order template
*OrderApi* | [**create_contract_note_from_order**](docs/OrderApi.md#create_contract_note_from_order) | **POST** /Order/Factory/createContractNoteFromOrder | Create contract note from order
*OrderApi* | [**create_order**](docs/OrderApi.md#create_order) | **POST** /Order/Factory/saveOrder | Create a new order
*OrderApi* | [**create_packing_list_from_order**](docs/OrderApi.md#create_packing_list_from_order) | **POST** /Order/Factory/createPackingListFromOrder | Create packing list from order
*OrderApi* | [**delete_order**](docs/OrderApi.md#delete_order) | **DELETE** /Order/{orderId} | Deletes an order
*OrderApi* | [**get_discounts**](docs/OrderApi.md#get_discounts) | **GET** /Order/{orderId}/getDiscounts | Find order discounts
*OrderApi* | [**get_order_by_id**](docs/OrderApi.md#get_order_by_id) | **GET** /Order/{orderId} | Find order by ID
*OrderApi* | [**get_order_positions_by_id**](docs/OrderApi.md#get_order_positions_by_id) | **GET** /Order/{orderId}/getPositions | Find order positions
*OrderApi* | [**get_orders**](docs/OrderApi.md#get_orders) | **GET** /Order | Retrieve orders
*OrderApi* | [**get_related_objects**](docs/OrderApi.md#get_related_objects) | **GET** /Order/{orderId}/getRelatedObjects | Find related objects
*OrderApi* | [**order_get_pdf**](docs/OrderApi.md#order_get_pdf) | **GET** /Order/{orderId}/getPdf | Retrieve pdf document of an order
*OrderApi* | [**order_send_by**](docs/OrderApi.md#order_send_by) | **PUT** /Order/{orderId}/sendBy | Mark order as sent
*OrderApi* | [**sendorder_via_e_mail**](docs/OrderApi.md#sendorder_via_e_mail) | **POST** /Order/{orderId}/sendViaEmail | Send order via email
*OrderApi* | [**update_order**](docs/OrderApi.md#update_order) | **PUT** /Order/{orderId} | Update an existing order
*OrderPosApi* | [**delete_order_pos**](docs/OrderPosApi.md#delete_order_pos) | **DELETE** /OrderPos/{orderPosId} | Deletes an order Position
*OrderPosApi* | [**get_order_position_by_id**](docs/OrderPosApi.md#get_order_position_by_id) | **GET** /OrderPos/{orderPosId} | Find order position by ID
*OrderPosApi* | [**get_order_positions**](docs/OrderPosApi.md#get_order_positions) | **GET** /OrderPos | Retrieve order positions
*OrderPosApi* | [**update_order_position**](docs/OrderPosApi.md#update_order_position) | **PUT** /OrderPos/{orderPosId} | Update an existing order position
*PartApi* | [**create_part**](docs/PartApi.md#create_part) | **POST** /Part | Create a new part
*PartApi* | [**get_part_by_id**](docs/PartApi.md#get_part_by_id) | **GET** /Part/{partId} | Find part by ID
*PartApi* | [**get_parts**](docs/PartApi.md#get_parts) | **GET** /Part | Retrieve parts
*PartApi* | [**part_get_stock**](docs/PartApi.md#part_get_stock) | **GET** /Part/{partId}/getStock | Get stock of a part
*PartApi* | [**update_part**](docs/PartApi.md#update_part) | **PUT** /Part/{partId} | Update an existing part
*ReportApi* | [**report_contact**](docs/ReportApi.md#report_contact) | **GET** /Report/contactlist | Export contact list
*ReportApi* | [**report_invoice**](docs/ReportApi.md#report_invoice) | **GET** /Report/invoicelist | Export invoice list
*ReportApi* | [**report_order**](docs/ReportApi.md#report_order) | **GET** /Report/orderlist | Export order list
*ReportApi* | [**report_voucher**](docs/ReportApi.md#report_voucher) | **GET** /Report/voucherlist | Export voucher list
*TagApi* | [**create_tag**](docs/TagApi.md#create_tag) | **POST** /Tag/Factory/create | Create a new tag
*TagApi* | [**delete_tag**](docs/TagApi.md#delete_tag) | **DELETE** /Tag/{tagId} | Deletes a tag
*TagApi* | [**get_tag_by_id**](docs/TagApi.md#get_tag_by_id) | **GET** /Tag/{tagId} | Find tag by ID
*TagApi* | [**get_tag_relations**](docs/TagApi.md#get_tag_relations) | **GET** /TagRelation | Retrieve tag relations
*TagApi* | [**get_tags**](docs/TagApi.md#get_tags) | **GET** /Tag | Retrieve tags
*TagApi* | [**update_tag**](docs/TagApi.md#update_tag) | **PUT** /Tag/{tagId} | Update tag
*VoucherApi* | [**book_voucher**](docs/VoucherApi.md#book_voucher) | **PUT** /Voucher/{voucherId}/bookAmount | Book a voucher
*VoucherApi* | [**for_account_number**](docs/VoucherApi.md#for_account_number) | **GET** /ReceiptGuidance/forAccountNumber | Get guidance by account number
*VoucherApi* | [**for_all_accounts**](docs/VoucherApi.md#for_all_accounts) | **GET** /ReceiptGuidance/forAllAccounts | Get all account guides
*VoucherApi* | [**for_expense**](docs/VoucherApi.md#for_expense) | **GET** /ReceiptGuidance/forExpense | Get guidance for expense accounts
*VoucherApi* | [**for_revenue**](docs/VoucherApi.md#for_revenue) | **GET** /ReceiptGuidance/forRevenue | Get guidance for revenue accounts
*VoucherApi* | [**for_tax_rule**](docs/VoucherApi.md#for_tax_rule) | **GET** /ReceiptGuidance/forTaxRule | Get guidance by Tax Rule
*VoucherApi* | [**get_voucher_by_id**](docs/VoucherApi.md#get_voucher_by_id) | **GET** /Voucher/{voucherId} | Find voucher by ID
*VoucherApi* | [**get_vouchers**](docs/VoucherApi.md#get_vouchers) | **GET** /Voucher | Retrieve vouchers
*VoucherApi* | [**update_voucher**](docs/VoucherApi.md#update_voucher) | **PUT** /Voucher/{voucherId} | Update an existing voucher
*VoucherApi* | [**voucher_enshrine**](docs/VoucherApi.md#voucher_enshrine) | **PUT** /Voucher/{voucherId}/enshrine | Enshrine
*VoucherApi* | [**voucher_factory_save_voucher**](docs/VoucherApi.md#voucher_factory_save_voucher) | **POST** /Voucher/Factory/saveVoucher | Create a new voucher
*VoucherApi* | [**voucher_reset_to_draft**](docs/VoucherApi.md#voucher_reset_to_draft) | **PUT** /Voucher/{voucherId}/resetToDraft | Reset status to draft
*VoucherApi* | [**voucher_reset_to_open**](docs/VoucherApi.md#voucher_reset_to_open) | **PUT** /Voucher/{voucherId}/resetToOpen | Reset status to open
*VoucherApi* | [**voucher_upload_file**](docs/VoucherApi.md#voucher_upload_file) | **POST** /Voucher/Factory/uploadTempFile | Upload voucher file
*VoucherPosApi* | [**get_voucher_positions**](docs/VoucherPosApi.md#get_voucher_positions) | **GET** /VoucherPos | Retrieve voucher positions


## Documentation For Models

 - [BookCreditNote200Response](docs/BookCreditNote200Response.md)
 - [BookCreditNote200ResponseCreditNote](docs/BookCreditNote200ResponseCreditNote.md)
 - [BookCreditNote200ResponseSevClient](docs/BookCreditNote200ResponseSevClient.md)
 - [BookCreditNoteRequest](docs/BookCreditNoteRequest.md)
 - [BookCreditNoteRequestCheckAccount](docs/BookCreditNoteRequestCheckAccount.md)
 - [BookCreditNoteRequestCheckAccountTransaction](docs/BookCreditNoteRequestCheckAccountTransaction.md)
 - [BookInvoice200Response](docs/BookInvoice200Response.md)
 - [BookInvoice200ResponseCreditNote](docs/BookInvoice200ResponseCreditNote.md)
 - [BookInvoice200ResponseSevClient](docs/BookInvoice200ResponseSevClient.md)
 - [BookInvoiceRequest](docs/BookInvoiceRequest.md)
 - [BookInvoiceRequestCheckAccountTransaction](docs/BookInvoiceRequestCheckAccountTransaction.md)
 - [BookVoucher200Response](docs/BookVoucher200Response.md)
 - [BookVoucher200ResponseCreditNote](docs/BookVoucher200ResponseCreditNote.md)
 - [BookVoucherRequest](docs/BookVoucherRequest.md)
 - [BookVoucherRequestCheckAccountTransaction](docs/BookVoucherRequestCheckAccountTransaction.md)
 - [BookkeepingSystemVersion200Response](docs/BookkeepingSystemVersion200Response.md)
 - [BookkeepingSystemVersion200ResponseObjects](docs/BookkeepingSystemVersion200ResponseObjects.md)
 - [CheckAccountTransactionEnshrine200Response](docs/CheckAccountTransactionEnshrine200Response.md)
 - [ContactCustomerNumberAvailabilityCheck200Response](docs/ContactCustomerNumberAvailabilityCheck200Response.md)
 - [CreateClearingAccount](docs/CreateClearingAccount.md)
 - [CreateClearingAccount201Response](docs/CreateClearingAccount201Response.md)
 - [CreateClearingAccountResponse](docs/CreateClearingAccountResponse.md)
 - [CreateCreditNoteFromInvoice201Response](docs/CreateCreditNoteFromInvoice201Response.md)
 - [CreateCreditNoteFromInvoice201ResponseObjects](docs/CreateCreditNoteFromInvoice201ResponseObjects.md)
 - [CreateCreditNoteFromInvoiceRequest](docs/CreateCreditNoteFromInvoiceRequest.md)
 - [CreateCreditNoteFromInvoiceRequestInvoice](docs/CreateCreditNoteFromInvoiceRequestInvoice.md)
 - [CreateCreditNoteFromVoucherRequest](docs/CreateCreditNoteFromVoucherRequest.md)
 - [CreateCreditNoteFromVoucherRequestVoucher](docs/CreateCreditNoteFromVoucherRequestVoucher.md)
 - [CreateFileImportAccount](docs/CreateFileImportAccount.md)
 - [CreateFileImportAccount201Response](docs/CreateFileImportAccount201Response.md)
 - [CreateFileImportAccountResponse](docs/CreateFileImportAccountResponse.md)
 - [CreateFileImportAccountResponseSevClient](docs/CreateFileImportAccountResponseSevClient.md)
 - [CreateInvoiceReminderRequest](docs/CreateInvoiceReminderRequest.md)
 - [CreateInvoiceReminderRequestInvoice](docs/CreateInvoiceReminderRequestInvoice.md)
 - [CreateTagRequest](docs/CreateTagRequest.md)
 - [CreateTagRequestObject](docs/CreateTagRequestObject.md)
 - [CreditNoteGetPdf200Response](docs/CreditNoteGetPdf200Response.md)
 - [CreditNoteResetToDraft200Response](docs/CreditNoteResetToDraft200Response.md)
 - [CreditNoteResetToDraft200ResponseObjects](docs/CreditNoteResetToDraft200ResponseObjects.md)
 - [CreditNoteResetToOpen200Response](docs/CreditNoteResetToOpen200Response.md)
 - [CreditNoteResetToOpen200ResponseObjects](docs/CreditNoteResetToOpen200ResponseObjects.md)
 - [CreditNoteSendByRequest](docs/CreditNoteSendByRequest.md)
 - [DeleteCheckAccount200Response](docs/DeleteCheckAccount200Response.md)
 - [ExportContact200Response](docs/ExportContact200Response.md)
 - [ExportContact200ResponseObjects](docs/ExportContact200ResponseObjects.md)
 - [ExportContactSevQueryParameter](docs/ExportContactSevQueryParameter.md)
 - [ExportContactSevQueryParameterFilter](docs/ExportContactSevQueryParameterFilter.md)
 - [ExportContactSevQueryParameterFilterCountry](docs/ExportContactSevQueryParameterFilterCountry.md)
 - [ExportCreditNote200Response](docs/ExportCreditNote200Response.md)
 - [ExportCreditNote200ResponseObjects](docs/ExportCreditNote200ResponseObjects.md)
 - [ExportCreditNoteSevQueryParameter](docs/ExportCreditNoteSevQueryParameter.md)
 - [ExportCreditNoteSevQueryParameterFilter](docs/ExportCreditNoteSevQueryParameterFilter.md)
 - [ExportCreditNoteSevQueryParameterFilterContact](docs/ExportCreditNoteSevQueryParameterFilterContact.md)
 - [ExportInvoice200Response](docs/ExportInvoice200Response.md)
 - [ExportInvoice200ResponseObjects](docs/ExportInvoice200ResponseObjects.md)
 - [ExportInvoiceSevQueryParameter](docs/ExportInvoiceSevQueryParameter.md)
 - [ExportInvoiceSevQueryParameterFilter](docs/ExportInvoiceSevQueryParameterFilter.md)
 - [ExportInvoiceSevQueryParameterFilterContact](docs/ExportInvoiceSevQueryParameterFilterContact.md)
 - [ExportInvoiceZip200Response](docs/ExportInvoiceZip200Response.md)
 - [ExportInvoiceZip200ResponseObjects](docs/ExportInvoiceZip200ResponseObjects.md)
 - [ExportInvoiceZipSevQueryParameter](docs/ExportInvoiceZipSevQueryParameter.md)
 - [ExportTransactions200Response](docs/ExportTransactions200Response.md)
 - [ExportTransactions200ResponseObjects](docs/ExportTransactions200ResponseObjects.md)
 - [ExportTransactionsSevQueryParameter](docs/ExportTransactionsSevQueryParameter.md)
 - [ExportTransactionsSevQueryParameterFilter](docs/ExportTransactionsSevQueryParameterFilter.md)
 - [ExportTransactionsSevQueryParameterFilterCheckAccount](docs/ExportTransactionsSevQueryParameterFilterCheckAccount.md)
 - [ExportVoucher200Response](docs/ExportVoucher200Response.md)
 - [ExportVoucherSevQueryParameter](docs/ExportVoucherSevQueryParameter.md)
 - [ExportVoucherSevQueryParameterFilter](docs/ExportVoucherSevQueryParameterFilter.md)
 - [ExportVoucherSevQueryParameterFilterContact](docs/ExportVoucherSevQueryParameterFilterContact.md)
 - [ExportVoucherZip200Response](docs/ExportVoucherZip200Response.md)
 - [ExportVoucherZip200ResponseObjects](docs/ExportVoucherZip200ResponseObjects.md)
 - [ExportVoucherZipSevQueryParameter](docs/ExportVoucherZipSevQueryParameter.md)
 - [ExportVoucherZipSevQueryParameterFilter](docs/ExportVoucherZipSevQueryParameterFilter.md)
 - [ExportVoucherZipSevQueryParameterFilterContact](docs/ExportVoucherZipSevQueryParameterFilterContact.md)
 - [FindContactsByCustomFieldValue200Response](docs/FindContactsByCustomFieldValue200Response.md)
 - [ForAllAccounts200Response](docs/ForAllAccounts200Response.md)
 - [GetAccountingContact200Response](docs/GetAccountingContact200Response.md)
 - [GetBalanceAtDate200Response](docs/GetBalanceAtDate200Response.md)
 - [GetCheckAccounts200Response](docs/GetCheckAccounts200Response.md)
 - [GetCommunicationWayKeys200Response](docs/GetCommunicationWayKeys200Response.md)
 - [GetCommunicationWayKeys200ResponseObjectsInner](docs/GetCommunicationWayKeys200ResponseObjectsInner.md)
 - [GetCommunicationWays200Response](docs/GetCommunicationWays200Response.md)
 - [GetContactAddresses200Response](docs/GetContactAddresses200Response.md)
 - [GetContactFieldSettings200Response](docs/GetContactFieldSettings200Response.md)
 - [GetContactFields200Response](docs/GetContactFields200Response.md)
 - [GetContactTabsItemCountById200Response](docs/GetContactTabsItemCountById200Response.md)
 - [GetCreditNotes200Response](docs/GetCreditNotes200Response.md)
 - [GetDiscounts200Response](docs/GetDiscounts200Response.md)
 - [GetInvoicePositionsById200Response](docs/GetInvoicePositionsById200Response.md)
 - [GetInvoices200Response](docs/GetInvoices200Response.md)
 - [GetLetterpapersWithThumb200Response](docs/GetLetterpapersWithThumb200Response.md)
 - [GetLetterpapersWithThumb200ResponseLetterpapersInner](docs/GetLetterpapersWithThumb200ResponseLetterpapersInner.md)
 - [GetNextCustomerNumber200Response](docs/GetNextCustomerNumber200Response.md)
 - [GetOrderPositionsById200Response](docs/GetOrderPositionsById200Response.md)
 - [GetOrders200Response](docs/GetOrders200Response.md)
 - [GetParts200Response](docs/GetParts200Response.md)
 - [GetPlaceholder200Response](docs/GetPlaceholder200Response.md)
 - [GetReferenceCount200Response](docs/GetReferenceCount200Response.md)
 - [GetTagRelations200Response](docs/GetTagRelations200Response.md)
 - [GetTags200Response](docs/GetTags200Response.md)
 - [GetTemplates200Response](docs/GetTemplates200Response.md)
 - [GetTemplates200ResponseTemplatesInner](docs/GetTemplates200ResponseTemplatesInner.md)
 - [GetTransactions200Response](docs/GetTransactions200Response.md)
 - [GetVoucherPositions200Response](docs/GetVoucherPositions200Response.md)
 - [GetVouchers200Response](docs/GetVouchers200Response.md)
 - [GetcreditNotePositions200Response](docs/GetcreditNotePositions200Response.md)
 - [InvoiceGetPdf200Response](docs/InvoiceGetPdf200Response.md)
 - [InvoiceGetXml200Response](docs/InvoiceGetXml200Response.md)
 - [InvoiceRender201Response](docs/InvoiceRender201Response.md)
 - [InvoiceRender201ResponseParametersInner](docs/InvoiceRender201ResponseParametersInner.md)
 - [InvoiceRender201ResponseParametersInnerValuesInner](docs/InvoiceRender201ResponseParametersInnerValuesInner.md)
 - [InvoiceRenderRequest](docs/InvoiceRenderRequest.md)
 - [InvoiceResetToDraft200Response](docs/InvoiceResetToDraft200Response.md)
 - [InvoiceResetToDraft200ResponseObjects](docs/InvoiceResetToDraft200ResponseObjects.md)
 - [InvoiceResetToOpen200Response](docs/InvoiceResetToOpen200Response.md)
 - [InvoiceResetToOpen200ResponseObjects](docs/InvoiceResetToOpen200ResponseObjects.md)
 - [InvoiceSendByRequest](docs/InvoiceSendByRequest.md)
 - [ModelAccountingContact](docs/ModelAccountingContact.md)
 - [ModelAccountingContactContact](docs/ModelAccountingContactContact.md)
 - [ModelAccountingContactResponse](docs/ModelAccountingContactResponse.md)
 - [ModelAccountingContactResponseContact](docs/ModelAccountingContactResponseContact.md)
 - [ModelAccountingContactResponseSevClient](docs/ModelAccountingContactResponseSevClient.md)
 - [ModelAccountingContactUpdate](docs/ModelAccountingContactUpdate.md)
 - [ModelAccountingContactUpdateContact](docs/ModelAccountingContactUpdateContact.md)
 - [ModelChangeLayout](docs/ModelChangeLayout.md)
 - [ModelChangeLayoutResponse](docs/ModelChangeLayoutResponse.md)
 - [ModelChangeLayoutResponseMetadaten](docs/ModelChangeLayoutResponseMetadaten.md)
 - [ModelChangeLayoutResponseMetadatenThumbsInner](docs/ModelChangeLayoutResponseMetadatenThumbsInner.md)
 - [ModelChangeLayoutResponseMetadatenThumbsInnerValuesInner](docs/ModelChangeLayoutResponseMetadatenThumbsInnerValuesInner.md)
 - [ModelCheckAccountResponse](docs/ModelCheckAccountResponse.md)
 - [ModelCheckAccountResponseSevClient](docs/ModelCheckAccountResponseSevClient.md)
 - [ModelCheckAccountTransaction](docs/ModelCheckAccountTransaction.md)
 - [ModelCheckAccountTransactionCheckAccount](docs/ModelCheckAccountTransactionCheckAccount.md)
 - [ModelCheckAccountTransactionResponse](docs/ModelCheckAccountTransactionResponse.md)
 - [ModelCheckAccountTransactionResponseCheckAccount](docs/ModelCheckAccountTransactionResponseCheckAccount.md)
 - [ModelCheckAccountTransactionResponseSevClient](docs/ModelCheckAccountTransactionResponseSevClient.md)
 - [ModelCheckAccountTransactionResponseSourceTransaction](docs/ModelCheckAccountTransactionResponseSourceTransaction.md)
 - [ModelCheckAccountTransactionResponseTargetTransaction](docs/ModelCheckAccountTransactionResponseTargetTransaction.md)
 - [ModelCheckAccountTransactionSevClient](docs/ModelCheckAccountTransactionSevClient.md)
 - [ModelCheckAccountTransactionSourceTransaction](docs/ModelCheckAccountTransactionSourceTransaction.md)
 - [ModelCheckAccountTransactionTargetTransaction](docs/ModelCheckAccountTransactionTargetTransaction.md)
 - [ModelCheckAccountTransactionUpdate](docs/ModelCheckAccountTransactionUpdate.md)
 - [ModelCheckAccountTransactionUpdateCheckAccount](docs/ModelCheckAccountTransactionUpdateCheckAccount.md)
 - [ModelCheckAccountUpdate](docs/ModelCheckAccountUpdate.md)
 - [ModelCommunicationWay](docs/ModelCommunicationWay.md)
 - [ModelCommunicationWayContact](docs/ModelCommunicationWayContact.md)
 - [ModelCommunicationWayKey](docs/ModelCommunicationWayKey.md)
 - [ModelCommunicationWayResponse](docs/ModelCommunicationWayResponse.md)
 - [ModelCommunicationWayResponseContact](docs/ModelCommunicationWayResponseContact.md)
 - [ModelCommunicationWayResponseKey](docs/ModelCommunicationWayResponseKey.md)
 - [ModelCommunicationWayResponseSevClient](docs/ModelCommunicationWayResponseSevClient.md)
 - [ModelCommunicationWaySevClient](docs/ModelCommunicationWaySevClient.md)
 - [ModelCommunicationWayUpdate](docs/ModelCommunicationWayUpdate.md)
 - [ModelCommunicationWayUpdateContact](docs/ModelCommunicationWayUpdateContact.md)
 - [ModelCommunicationWayUpdateKey](docs/ModelCommunicationWayUpdateKey.md)
 - [ModelContact](docs/ModelContact.md)
 - [ModelContactAddress](docs/ModelContactAddress.md)
 - [ModelContactAddressResponse](docs/ModelContactAddressResponse.md)
 - [ModelContactAddressResponseCategory](docs/ModelContactAddressResponseCategory.md)
 - [ModelContactAddressResponseContact](docs/ModelContactAddressResponseContact.md)
 - [ModelContactAddressResponseCountry](docs/ModelContactAddressResponseCountry.md)
 - [ModelContactAddressResponseSevClient](docs/ModelContactAddressResponseSevClient.md)
 - [ModelContactAddressUpdate](docs/ModelContactAddressUpdate.md)
 - [ModelContactAddressUpdateContact](docs/ModelContactAddressUpdateContact.md)
 - [ModelContactAddressUpdateCountry](docs/ModelContactAddressUpdateCountry.md)
 - [ModelContactCategory](docs/ModelContactCategory.md)
 - [ModelContactCustomField](docs/ModelContactCustomField.md)
 - [ModelContactCustomFieldContact](docs/ModelContactCustomFieldContact.md)
 - [ModelContactCustomFieldContactCustomFieldSetting](docs/ModelContactCustomFieldContactCustomFieldSetting.md)
 - [ModelContactCustomFieldResponse](docs/ModelContactCustomFieldResponse.md)
 - [ModelContactCustomFieldResponseContact](docs/ModelContactCustomFieldResponseContact.md)
 - [ModelContactCustomFieldResponseSevClient](docs/ModelContactCustomFieldResponseSevClient.md)
 - [ModelContactCustomFieldSetting](docs/ModelContactCustomFieldSetting.md)
 - [ModelContactCustomFieldSettingResponse](docs/ModelContactCustomFieldSettingResponse.md)
 - [ModelContactCustomFieldSettingResponseSevClient](docs/ModelContactCustomFieldSettingResponseSevClient.md)
 - [ModelContactCustomFieldSettingUpdate](docs/ModelContactCustomFieldSettingUpdate.md)
 - [ModelContactCustomFieldUpdate](docs/ModelContactCustomFieldUpdate.md)
 - [ModelContactCustomFieldUpdateContactCustomFieldSetting](docs/ModelContactCustomFieldUpdateContactCustomFieldSetting.md)
 - [ModelContactParent](docs/ModelContactParent.md)
 - [ModelContactResponse](docs/ModelContactResponse.md)
 - [ModelContactResponseCategory](docs/ModelContactResponseCategory.md)
 - [ModelContactResponseParent](docs/ModelContactResponseParent.md)
 - [ModelContactResponseSevClient](docs/ModelContactResponseSevClient.md)
 - [ModelContactUpdate](docs/ModelContactUpdate.md)
 - [ModelContactUpdateCategory](docs/ModelContactUpdateCategory.md)
 - [ModelContactUpdateParent](docs/ModelContactUpdateParent.md)
 - [ModelCreateInvoiceFromOrder](docs/ModelCreateInvoiceFromOrder.md)
 - [ModelCreateInvoiceFromOrderOrder](docs/ModelCreateInvoiceFromOrderOrder.md)
 - [ModelCreatePackingListFromOrder](docs/ModelCreatePackingListFromOrder.md)
 - [ModelCreditNote](docs/ModelCreditNote.md)
 - [ModelCreditNoteAddressCountry](docs/ModelCreditNoteAddressCountry.md)
 - [ModelCreditNoteContact](docs/ModelCreditNoteContact.md)
 - [ModelCreditNoteContactPerson](docs/ModelCreditNoteContactPerson.md)
 - [ModelCreditNoteCreateUser](docs/ModelCreditNoteCreateUser.md)
 - [ModelCreditNoteMailResponse](docs/ModelCreditNoteMailResponse.md)
 - [ModelCreditNoteMailResponseSevClient](docs/ModelCreditNoteMailResponseSevClient.md)
 - [ModelCreditNotePos](docs/ModelCreditNotePos.md)
 - [ModelCreditNotePosCreditNote](docs/ModelCreditNotePosCreditNote.md)
 - [ModelCreditNotePosPart](docs/ModelCreditNotePosPart.md)
 - [ModelCreditNotePosResponse](docs/ModelCreditNotePosResponse.md)
 - [ModelCreditNotePosResponseCreditNote](docs/ModelCreditNotePosResponseCreditNote.md)
 - [ModelCreditNotePosResponsePart](docs/ModelCreditNotePosResponsePart.md)
 - [ModelCreditNotePosResponseSevClient](docs/ModelCreditNotePosResponseSevClient.md)
 - [ModelCreditNotePosResponseUnity](docs/ModelCreditNotePosResponseUnity.md)
 - [ModelCreditNotePosSevClient](docs/ModelCreditNotePosSevClient.md)
 - [ModelCreditNotePosUnity](docs/ModelCreditNotePosUnity.md)
 - [ModelCreditNoteResponse](docs/ModelCreditNoteResponse.md)
 - [ModelCreditNoteResponseAddressCountry](docs/ModelCreditNoteResponseAddressCountry.md)
 - [ModelCreditNoteResponseContact](docs/ModelCreditNoteResponseContact.md)
 - [ModelCreditNoteResponseContactPerson](docs/ModelCreditNoteResponseContactPerson.md)
 - [ModelCreditNoteResponseCreateUser](docs/ModelCreditNoteResponseCreateUser.md)
 - [ModelCreditNoteResponseSevClient](docs/ModelCreditNoteResponseSevClient.md)
 - [ModelCreditNoteResponseTaxRule](docs/ModelCreditNoteResponseTaxRule.md)
 - [ModelCreditNoteResponseTaxSet](docs/ModelCreditNoteResponseTaxSet.md)
 - [ModelCreditNoteSendByWithRender](docs/ModelCreditNoteSendByWithRender.md)
 - [ModelCreditNoteSevClient](docs/ModelCreditNoteSevClient.md)
 - [ModelCreditNoteTaxSet](docs/ModelCreditNoteTaxSet.md)
 - [ModelCreditNoteUpdate](docs/ModelCreditNoteUpdate.md)
 - [ModelCreditNoteUpdateContact](docs/ModelCreditNoteUpdateContact.md)
 - [ModelCreditNoteUpdateContactPerson](docs/ModelCreditNoteUpdateContactPerson.md)
 - [ModelDiscount](docs/ModelDiscount.md)
 - [ModelDiscountObject](docs/ModelDiscountObject.md)
 - [ModelDiscountsResponse](docs/ModelDiscountsResponse.md)
 - [ModelEmail](docs/ModelEmail.md)
 - [ModelEmailOrder](docs/ModelEmailOrder.md)
 - [ModelEmailSevClient](docs/ModelEmailSevClient.md)
 - [ModelInvoice](docs/ModelInvoice.md)
 - [ModelInvoiceAddressCountry](docs/ModelInvoiceAddressCountry.md)
 - [ModelInvoiceContact](docs/ModelInvoiceContact.md)
 - [ModelInvoiceContactPerson](docs/ModelInvoiceContactPerson.md)
 - [ModelInvoiceOrigin](docs/ModelInvoiceOrigin.md)
 - [ModelInvoicePaymentMethod](docs/ModelInvoicePaymentMethod.md)
 - [ModelInvoicePos](docs/ModelInvoicePos.md)
 - [ModelInvoicePosInvoice](docs/ModelInvoicePosInvoice.md)
 - [ModelInvoicePosResponse](docs/ModelInvoicePosResponse.md)
 - [ModelInvoicePosResponseInvoice](docs/ModelInvoicePosResponseInvoice.md)
 - [ModelInvoicePosResponsePart](docs/ModelInvoicePosResponsePart.md)
 - [ModelInvoicePosResponseSevClient](docs/ModelInvoicePosResponseSevClient.md)
 - [ModelInvoicePosResponseUnity](docs/ModelInvoicePosResponseUnity.md)
 - [ModelInvoicePosSevClient](docs/ModelInvoicePosSevClient.md)
 - [ModelInvoicePosUnity](docs/ModelInvoicePosUnity.md)
 - [ModelInvoiceResponse](docs/ModelInvoiceResponse.md)
 - [ModelInvoiceResponseAddressCountry](docs/ModelInvoiceResponseAddressCountry.md)
 - [ModelInvoiceResponseContact](docs/ModelInvoiceResponseContact.md)
 - [ModelInvoiceResponseContactPerson](docs/ModelInvoiceResponseContactPerson.md)
 - [ModelInvoiceResponseCostCentre](docs/ModelInvoiceResponseCostCentre.md)
 - [ModelInvoiceResponseOrigin](docs/ModelInvoiceResponseOrigin.md)
 - [ModelInvoiceResponsePaymentMethod](docs/ModelInvoiceResponsePaymentMethod.md)
 - [ModelInvoiceResponseSevClient](docs/ModelInvoiceResponseSevClient.md)
 - [ModelInvoiceResponseTaxSet](docs/ModelInvoiceResponseTaxSet.md)
 - [ModelInvoiceSevClient](docs/ModelInvoiceSevClient.md)
 - [ModelInvoiceTaxSet](docs/ModelInvoiceTaxSet.md)
 - [ModelOrder](docs/ModelOrder.md)
 - [ModelOrderAddressCountry](docs/ModelOrderAddressCountry.md)
 - [ModelOrderContact](docs/ModelOrderContact.md)
 - [ModelOrderContactPerson](docs/ModelOrderContactPerson.md)
 - [ModelOrderOrigin](docs/ModelOrderOrigin.md)
 - [ModelOrderPos](docs/ModelOrderPos.md)
 - [ModelOrderPosOrder](docs/ModelOrderPosOrder.md)
 - [ModelOrderPosResponse](docs/ModelOrderPosResponse.md)
 - [ModelOrderPosResponseOrder](docs/ModelOrderPosResponseOrder.md)
 - [ModelOrderPosResponsePart](docs/ModelOrderPosResponsePart.md)
 - [ModelOrderPosResponseSevClient](docs/ModelOrderPosResponseSevClient.md)
 - [ModelOrderPosResponseUnity](docs/ModelOrderPosResponseUnity.md)
 - [ModelOrderPosSevClient](docs/ModelOrderPosSevClient.md)
 - [ModelOrderPosUpdate](docs/ModelOrderPosUpdate.md)
 - [ModelOrderResponse](docs/ModelOrderResponse.md)
 - [ModelOrderResponseAddressCountry](docs/ModelOrderResponseAddressCountry.md)
 - [ModelOrderResponseContact](docs/ModelOrderResponseContact.md)
 - [ModelOrderResponseContactPerson](docs/ModelOrderResponseContactPerson.md)
 - [ModelOrderResponseCreateUser](docs/ModelOrderResponseCreateUser.md)
 - [ModelOrderResponseOrigin](docs/ModelOrderResponseOrigin.md)
 - [ModelOrderResponseSevClient](docs/ModelOrderResponseSevClient.md)
 - [ModelOrderResponseTaxSet](docs/ModelOrderResponseTaxSet.md)
 - [ModelOrderTaxSet](docs/ModelOrderTaxSet.md)
 - [ModelOrderUpdate](docs/ModelOrderUpdate.md)
 - [ModelOrderUpdateAddressCountry](docs/ModelOrderUpdateAddressCountry.md)
 - [ModelOrderUpdateContact](docs/ModelOrderUpdateContact.md)
 - [ModelOrderUpdateContactPerson](docs/ModelOrderUpdateContactPerson.md)
 - [ModelOrderUpdateCreateUser](docs/ModelOrderUpdateCreateUser.md)
 - [ModelOrderUpdateSevClient](docs/ModelOrderUpdateSevClient.md)
 - [ModelOrderUpdateTaxSet](docs/ModelOrderUpdateTaxSet.md)
 - [ModelPart](docs/ModelPart.md)
 - [ModelPartCategory](docs/ModelPartCategory.md)
 - [ModelPartSevClient](docs/ModelPartSevClient.md)
 - [ModelPartUnity](docs/ModelPartUnity.md)
 - [ModelPartUpdate](docs/ModelPartUpdate.md)
 - [ModelTagCreateResponse](docs/ModelTagCreateResponse.md)
 - [ModelTagCreateResponseTag](docs/ModelTagCreateResponseTag.md)
 - [ModelTagResponse](docs/ModelTagResponse.md)
 - [ModelTagResponseSevClient](docs/ModelTagResponseSevClient.md)
 - [ModelTextparserFetchDictionaryEntriesByTypeResponse](docs/ModelTextparserFetchDictionaryEntriesByTypeResponse.md)
 - [ModelTextparserFetchDictionaryEntriesByTypeResponseValueInner](docs/ModelTextparserFetchDictionaryEntriesByTypeResponseValueInner.md)
 - [ModelVoucher](docs/ModelVoucher.md)
 - [ModelVoucherCostCentre](docs/ModelVoucherCostCentre.md)
 - [ModelVoucherCreateUser](docs/ModelVoucherCreateUser.md)
 - [ModelVoucherDocument](docs/ModelVoucherDocument.md)
 - [ModelVoucherPos](docs/ModelVoucherPos.md)
 - [ModelVoucherPosAccountDatev](docs/ModelVoucherPosAccountDatev.md)
 - [ModelVoucherPosAccountingType](docs/ModelVoucherPosAccountingType.md)
 - [ModelVoucherPosEstimatedAccountingType](docs/ModelVoucherPosEstimatedAccountingType.md)
 - [ModelVoucherPosResponse](docs/ModelVoucherPosResponse.md)
 - [ModelVoucherPosResponseAccountingType](docs/ModelVoucherPosResponseAccountingType.md)
 - [ModelVoucherPosResponseEstimatedAccountingType](docs/ModelVoucherPosResponseEstimatedAccountingType.md)
 - [ModelVoucherPosResponseSevClient](docs/ModelVoucherPosResponseSevClient.md)
 - [ModelVoucherPosResponseVoucher](docs/ModelVoucherPosResponseVoucher.md)
 - [ModelVoucherPosSevClient](docs/ModelVoucherPosSevClient.md)
 - [ModelVoucherPosVoucher](docs/ModelVoucherPosVoucher.md)
 - [ModelVoucherResponse](docs/ModelVoucherResponse.md)
 - [ModelVoucherResponseCostCentre](docs/ModelVoucherResponseCostCentre.md)
 - [ModelVoucherResponseCreateUser](docs/ModelVoucherResponseCreateUser.md)
 - [ModelVoucherResponseDocument](docs/ModelVoucherResponseDocument.md)
 - [ModelVoucherResponseSevClient](docs/ModelVoucherResponseSevClient.md)
 - [ModelVoucherResponseSupplier](docs/ModelVoucherResponseSupplier.md)
 - [ModelVoucherResponseTaxSet](docs/ModelVoucherResponseTaxSet.md)
 - [ModelVoucherSevClient](docs/ModelVoucherSevClient.md)
 - [ModelVoucherSupplier](docs/ModelVoucherSupplier.md)
 - [ModelVoucherTaxRule](docs/ModelVoucherTaxRule.md)
 - [ModelVoucherTaxSet](docs/ModelVoucherTaxSet.md)
 - [ModelVoucherUpdate](docs/ModelVoucherUpdate.md)
 - [ModelVoucherUpdateSupplier](docs/ModelVoucherUpdateSupplier.md)
 - [ModelVoucherUpdateTaxSet](docs/ModelVoucherUpdateTaxSet.md)
 - [OrderGetPdf200Response](docs/OrderGetPdf200Response.md)
 - [OrderSendByRequest](docs/OrderSendByRequest.md)
 - [PartGetStock200Response](docs/PartGetStock200Response.md)
 - [ReceiptGuideDto](docs/ReceiptGuideDto.md)
 - [ReceiptGuideDtoAllowedTaxRulesInner](docs/ReceiptGuideDtoAllowedTaxRulesInner.md)
 - [ReportContact200Response](docs/ReportContact200Response.md)
 - [ReportContact200ResponseObjects](docs/ReportContact200ResponseObjects.md)
 - [ReportContactSevQueryParameter](docs/ReportContactSevQueryParameter.md)
 - [ReportInvoice200Response](docs/ReportInvoice200Response.md)
 - [ReportInvoice200ResponseObjects](docs/ReportInvoice200ResponseObjects.md)
 - [ReportInvoiceSevQueryParameter](docs/ReportInvoiceSevQueryParameter.md)
 - [ReportOrder200Response](docs/ReportOrder200Response.md)
 - [ReportOrder200ResponseObjects](docs/ReportOrder200ResponseObjects.md)
 - [ReportOrderSevQueryParameter](docs/ReportOrderSevQueryParameter.md)
 - [ReportOrderSevQueryParameterFilter](docs/ReportOrderSevQueryParameterFilter.md)
 - [ReportOrderSevQueryParameterFilterContact](docs/ReportOrderSevQueryParameterFilterContact.md)
 - [ReportVoucher200Response](docs/ReportVoucher200Response.md)
 - [ReportVoucher200ResponseObjects](docs/ReportVoucher200ResponseObjects.md)
 - [ReportVoucherSevQueryParameter](docs/ReportVoucherSevQueryParameter.md)
 - [SaveCreditNote](docs/SaveCreditNote.md)
 - [SaveCreditNoteCreditNotePosDelete](docs/SaveCreditNoteCreditNotePosDelete.md)
 - [SaveCreditNoteDiscountDelete](docs/SaveCreditNoteDiscountDelete.md)
 - [SaveCreditNoteDiscountSave](docs/SaveCreditNoteDiscountSave.md)
 - [SaveCreditNoteResponse](docs/SaveCreditNoteResponse.md)
 - [SaveInvoice](docs/SaveInvoice.md)
 - [SaveInvoiceDiscountDelete](docs/SaveInvoiceDiscountDelete.md)
 - [SaveInvoiceDiscountSaveInner](docs/SaveInvoiceDiscountSaveInner.md)
 - [SaveInvoiceInvoicePosDelete](docs/SaveInvoiceInvoicePosDelete.md)
 - [SaveInvoiceResponse](docs/SaveInvoiceResponse.md)
 - [SaveOrder](docs/SaveOrder.md)
 - [SaveOrderOrderPosDelete](docs/SaveOrderOrderPosDelete.md)
 - [SaveOrderResponse](docs/SaveOrderResponse.md)
 - [SaveVoucher](docs/SaveVoucher.md)
 - [SaveVoucherResponse](docs/SaveVoucherResponse.md)
 - [SaveVoucherVoucherPosDelete](docs/SaveVoucherVoucherPosDelete.md)
 - [SendCreditNoteViaEMail201Response](docs/SendCreditNoteViaEMail201Response.md)
 - [SendCreditNoteViaEMailRequest](docs/SendCreditNoteViaEMailRequest.md)
 - [SendInvoiceViaEMailRequest](docs/SendInvoiceViaEMailRequest.md)
 - [SendorderViaEMail201Response](docs/SendorderViaEMail201Response.md)
 - [SendorderViaEMailRequest](docs/SendorderViaEMailRequest.md)
 - [UpdateExportConfigRequest](docs/UpdateExportConfigRequest.md)
 - [UpdateTagRequest](docs/UpdateTagRequest.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorError](docs/ValidationErrorError.md)
 - [VoucherResetToOpen200Response](docs/VoucherResetToOpen200Response.md)
 - [VoucherResetToOpen200ResponseObjects](docs/VoucherResetToOpen200ResponseObjects.md)
 - [VoucherUploadFile201Response](docs/VoucherUploadFile201Response.md)
 - [VoucherUploadFile201ResponseObjects](docs/VoucherUploadFile201ResponseObjects.md)
 - [VoucherUploadFileRequest](docs/VoucherUploadFileRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="api_key"></a>
### api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




