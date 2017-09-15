<script src="/javascript/jquery.min.js"></script>
<form id="delete">
  <input id="target" type="text">
  <input type="submit">
</form>

<div id="images">
  <ul>
  %for l in files:
    <li>{{ l[:-4] }} <img src="/thumb/{{ l }}"></img></li>
  %end
  </ul>
</div>

<script>
  $(() => {
    $("#delete").on("change", () => {
      let file = $("#target").val()
      $.ajax({
        type: "POST",
        url: "/delete",
        data: {filename: file}
      }).done((msg) => {
        window.location.reload()
      })
    })
  })
</script>
