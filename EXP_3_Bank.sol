//SPDX-License-Identifier: MIT 
pragma solidity ^0.8.7;

// Created a smart contract that allows a user to deposit, withdraw and save ETH!! 

contract Bank{
    // we mapped the address of the caller balance in the contract 
    mapping(address => uint) public balances;

    // deposited value of the sender address is mapped in balance 
    function deposit() public payable{ 
        balances[msg.sender] += msg.value; 
    }
 
    // Function to witdraw amount
    function withdraw(uint amount) public{

        // Here check whether balance of the sender is less than amount if not then return Error
        require(balances[msg.sender] >= amount, "Not Enough ETH"); 
        
        // If amount satisfied then simply subtract it from the sender 
        balances[msg.sender] -= amount;
 
        //True bool is called to confirm the amount
        
        (bool sent,) = msg.sender.call{value: amount}("Sent"); 
        require(sent,"failed to send ETH");
 
    } 
    function getBal() public view returns(uint){ 
        return address(this).balance;
    }
}