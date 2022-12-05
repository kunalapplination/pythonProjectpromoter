
//<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
 $(document).ready(function () {
              $.ajax({
                type: "GET",
                url: "https://avp-backend.applination.in/public/index.php/api/getEventRegistrationDetail?id=8403",
                headers: {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXZwLWJhY2tlbmQuYXBwbGluYXRpb24uaW5cL3B1YmxpY1wvaW5kZXgucGhwXC9hcGlcL2xvZ2luUHJvbW90ZXIiLCJpYXQiOjE2Njg1ODA1MzYsImV4cCI6MTY2OTE4NTMzNiwibmJmIjoxNjY4NTgwNTM2LCJqdGkiOiJjVVFjWXo4bEp2ZkpUR0RSIiwic3ViIjoxMDAwMTAyNjUsInBydiI6IjBkM2NhNmI0Yzg4Mzk1NzhlYjc2NTg0YTkwOWM1YjMzMTMxZTcyMTUiLCJpZCI6MTAwMDEwMjY1LCJlbWFpbCI6ImthdXNoaWtpQGFwcGxpbmF0aW9uLmluIn0.ViPiBkCLq3H0z3i830xzgbB1d89FK0apdHjlDJABUxA"},
                success: function (result, status, xhr) {
                var responseData=result;
                console.log('responseData',responseData);
//                   result["name"]
                 },
                error: function (xhr, status, error) {
                    alert("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText)
                }
            });

    });