<html>
<head>
	<meta charset="utf-8" />
    <title>Login for setu</title>
    <!-- 新 Bootstrap4 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/4.1.0/css/bootstrap.min.css">

     <!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
     <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
 
     <!-- popper.min.js 用于弹窗、提示、下拉菜单 -->
    <script src="https://cdn.bootcss.com/popper.js/1.12.5/umd/popper.min.js"></script>
 
     <!-- 最新的 Bootstrap4 核心 JavaScript 文件 -->
<script src="https://cdn.bootcss.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
</head>

<body>
	<div style="margin-left:40%;">
		<h3>Login for setu</h3>
	</div>
<hr>
<form style="margin-left:36%;margin-top:200px;" method='GET'>
	<div class="form-group">
		<label for="user" stype="display:inline;">Username：</label>
		<input type="text" class="form-control" id="user" name='username' style="display:inline;width:200px;"autocomplete="off" />
	</div>
	<div class="form-group">
		<label for="password" stype="display:inline;">Password：</label>
		<input type="text" class="form-control" id="password" name='password' style="display:inline;width:200px;"autocomplete="off" />
	</div>
	<div>
		<button type="submit" class="btn btn-primary">Login</button>
	</div>
</form>

<!-- if (md5($_GET['username']) === md5($_GET['password'])) + if ($_GET['username'] == $_GET['password']) -->
<!-- you will get something cool! -->

</body>
</html>
<?php
error_reporting(0);

if (isset($_GET['username']) and isset($_GET['password'])) {
      if ($_GET['username'] == $_GET['password'])
            print 'no';
      else if (md5($_GET['username']) === md5($_GET['password']))
            header("Location: setu.php");
      else
            print 'Invalid password';
}

?>
