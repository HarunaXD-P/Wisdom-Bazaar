<!-- right side,for my information and menu -->
<template>
  <div class="_first" id="cai_msg_msg">
		<div id="cai_msg_img">
			<img
				src="../assets/logo.jpg"
				width="150px"
				height="112px"
			/><img />
		</div>
		<div id="cai_msg_idoth">
			<div id="cai_msg_name"> Cai </div>
			<div id="cai_msg_time"> 2021年11月11日（木）</div>
		</div>
		<div id="cai_msg_main">
			第一次世界大戦の終結から203年を祝うため、iphone 13は大幅に値下げされ、
			わずか9999元、先着順で、たっぷりとしたサプライズギフトになりました。 <br>
			<img
				src="../assets/iphone.jpeg"
			/><img />
		</div>
	</div>
</template>

<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

<style>
#cai_msg_msg {
	min-height: 112px;
	margin-left: 40px;
}
	
#cai_msg_img {
	width: 150px;
	height: 112px;
	margin: 0px;
	padding-top: 0px;
	border: 0px;
	background: none;
	float: left;
}

#cai_msg_idoth {
	height: 112px;
	width: 1000px;
	margin: 0px, 20px;
	float: left;
}

#cai_msg_name {
	height: 30px;
	font-size: 25px;
	text-align: left;
	position: relative;
	top: 57px;
}

#cai_msg_time {
	height: 25px;
	font-size: 15pt;
	text-align: left;
	position: relative;
	top: 57px;
}

#cai_msg_main {
	width: 1000px;
	margin-left: 77px;
	font-size: 30px;
	text-align: left;
}

</style>