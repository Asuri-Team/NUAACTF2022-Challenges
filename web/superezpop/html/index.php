<?php
error_reporting(0);
 
class User{
    public $username;
    public $password;
    public $variable;
    public $a;
    
    public function __construct()
    {
        $this->username = "user";
        $this->password = "user";
    }


    public function __wakeup(){
        if( ($this->username != $this->password) && (md5($this->username) === md5($this->password)) && (sha1($this->username)=== sha1($this->password)) ){
			echo "wuhu!";
			return $this->variable->xxx;
        }else{
			die("o^o");
        }
    }
}

class Login{
	public $point;
	
    public function __get($key){
		$func = $this->point;
		return $func();
    }	

}

class Read{
	public $filename;
	
    public function __invoke(){
		echo file_get_contents($this->filename.".php");
    }
}
 
if(isset($_GET['x'])){
    unserialize($_GET['x']);
}else{
	highlight_file(__FILE__);
}
?>