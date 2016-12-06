# Netconf_vRouter
Small Python script for testing/understanding Netconf RPC calls on vRouter

RPC Calls have been forged on 5.1R1 version Yang model and script use parmamiko library to enable ssh/netconf connection

## RPC calls

RPC calls used in this script :
  - Hello (base) : used after the connection to exchange capabilities between client/server

```
<?xml version="1.0" encoding="UTF-8"?>
  <hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <capabilities>
      <capability>urn:ietf:params:netconf:base:1.0</capability>
    </capabilities>
  </hello>
]]>]]>
```

- Ping (vyatta-op) : send to server to execute ping

```
<rpc message-id="r_msg" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<ping xmlns="urn:vyatta.com:mgmt:vyatta-op:1">
		<host>r_add</host>
  		<count>5</count>
		<ttl>3</ttl>
	</ping>
</rpc>
```  

- Route (vyatta-op) : send to server to get route

```
<rpc message-id="r_msg" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<route xmlns="urn:vyatta.com:mgmt:vyatta-op:1">
		<destination>r_add</destination>
	</route>
</rpc>
]]>]]>
```
  
  - Close (base) : used to close connection

```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <close-session/>
</rpc>
]]>]]>
```

## How to use

  1- Credentials : vRouter Hostname/Login/Password
  
  2- Hello exchange between client/server
  
  3- User can choose to perform rpc call or end script
  
  ```
  Do you want to pass some netconf rpc call ?
  y/n ?
  ```
  
  4- User can choose between Ping & Route :
  
  ```
  Ping (p) or Route (r) 
  p/r ?
  ```
  
  5- User provides @ip for ping or route
  
  ```
  @ip X.X.X.X :
  ```
  
  6- Rpc call is sent to vRouter, vRouter send back results
  
  7- User can choose to perform rpc call or end script

  ```
  Do you want to pass some netconf rpc call ?
  y/n ?
  ```  
  
  8- If end script is chosen, rpc close is sent to vRouter
  




