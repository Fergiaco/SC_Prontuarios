// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Paciente
 * @dev Store & retrieve value in a variable
 */
contract Paciente {
    
    struct infos {
    string dados;
    string cid;
    }

    infos public info;
    string public text;
    address public owner;
    infos[] prontuarios;

    constructor() {
        owner = msg.sender;
    }

    error Unauthorized();

    /// Function called too early.
    error TooEarly();

    /// Not enough Ether sent with function call.
    error NotEnoughEther();

    modifier onlyBy(address _account) {
        if (msg.sender != _account) revert("Essa conta nao tem permissao");
        _;
    }

    function add(string memory _dados, string memory _cid) public onlyBy(owner) {
        info=infos(_dados,_cid);
        prontuarios.push(info);
    }

    function remove(uint _index) public onlyBy(owner) {
        delete(prontuarios[_index]);
    }

    function get() public view onlyBy(owner)  returns (infos[] memory) {
        return prontuarios;
    }

}
