<link href="/css/croppie.css" rel="stylesheet" type="text/css" media="all"/>
<script src="/javascript/jquery.min.js"></script>
<script src="/javascript/croppie.js"></script>

<p>Hello</p>

<form id="file">
  <input type="file">
</form>

<form id="result">
  <input id="filename" type="text">
  <input type="submit" value="result">
</form>

<div id="crop">
  <img id="img" class="img-responsive" src="https://tpc.googlesyndication.com/simgad/10888799066484856782" alt="">
</div>

<script>
$(() => {
  $("#file").on("change", "input[type=file]", (e) => {
    let file = e.target.files[0]
    let reader = new FileReader()

    reader.onload = ((file) => {
      return (e) => {
        basic.croppie("bind", {
            url: e.target.result,
        });
      }
    })(file)
    reader.readAsDataURL(file)
  })

  let basic = $("#img").croppie({
    viewport: {
        width: 200,
        height: 200,
        type: "circle"
    }
  });

  $("#result").on("change", () => {
    basic.croppie("result", {
      type: "canvas",
      size: {width: 200, height: 200},
    }).then((res) => {
      $.ajax({
        type: "POST",
        url: "/save/" + $("#filename").val(),
        data: {src: res}
      }).done((msg) => {
        alert("success")
      })
    });
  });
})
</script>
