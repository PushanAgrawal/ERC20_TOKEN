// contracts/DUToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract DUToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("DUToken", "DUT") {
        _mint(msg.sender, initialSupply);
    }
}