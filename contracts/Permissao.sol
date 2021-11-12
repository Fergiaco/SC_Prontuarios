// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Paciente
 * @dev Store & retrieve value in a variable
 */
contract Permissao{
    address private owner;

    //combinacao de chaves para cid
    mapping(string => string[]) public cids;

    constructor(address _paciente) {
        owner = _paciente;
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

    function addPront(string memory _combinacao,string memory _cid) onlyBy(owner) public {
        cids[_combinacao].push(_cid);
    
    }

    function removePront(string memory _combinacao) onlyBy(owner) public {
        delete cids[_combinacao];
    
    }

    function get(string memory _combinacao) public view returns(string[] memory){
        return cids[_combinacao];
    }
}
