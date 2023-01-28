pragma solidity 0.8.7;

contract HiddenSecret1 {
	uint8 nonce;
	uint256[] public secrets;

	event isSolved();
	
    constructor(uint256 _secret) public {
		nonce = 0;
		secrets.push(_secret);
    }

    function guess(uint256 _answer) public {
		nonce = nonce + 1;
		require( nonce <= 3 );
        if( keccak256(abi.encodePacked(secrets[0])) == keccak256(abi.encodePacked(_answer)) ) {
			emit isSolved();
		}
    }
}
