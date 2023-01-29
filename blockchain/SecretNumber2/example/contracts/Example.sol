pragma solidity 0.8.7;

contract HiddenSecret2 {
	uint8 nonce;
	uint256[] private secrets;

	event isSolved();
	
    constructor(uint256 _secret) public {
		nonce = 0;
		secrets.push(uint256(keccak256(abi.encodePacked(_secret+block.number))));
    }

    function guess(uint256 _answer) public {
		require(tx.origin != msg.sender);
		nonce = nonce + 1;
		require( nonce <= 3 );
        if( keccak256(abi.encodePacked(secrets[0])) == keccak256(abi.encodePacked(_answer)) ) {
			emit isSolved();
		}
    }
}