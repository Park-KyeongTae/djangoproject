// 삭제 시 a 태그 중지
// confirm 확인
// 확인 시 지정한 href로 경로로 이동

const deleteAll = document.querySelectorAll(".delete");

deleteAll.forEach((item) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();

    const href = e.target.href;
    if (confirm("삭제 하시겠습니까?")) {
      location.href = href;
    }
  });
});
