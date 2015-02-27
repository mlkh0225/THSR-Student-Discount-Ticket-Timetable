# 台灣高鐵大學生優惠車次查詢

需求：Python 2.6 或更新<br>
<br>
高鐵提供大學生優惠五折、七折車次<br>
（http://www.thsrc.com.tw/tw/Article/ArticleContent/530e869c-479d-441a-a4b4-61a8166827e9）<br>
但網頁時刻表並沒有查詢功能，要找出適合車次常常看到眼花<br>
<br>
這個程式可以在輸入以下資訊後<br>
1、出發日期，格式為 yyyy/mm/dd<br>
2、出發時間，格式為 hh（24小時制）<br>
3、時間區間，格式為 hh<br>
4、起站代號<br>
5、訖站代號<br>
提供符合的車次<br>
<br>
以下為執行結果：<br>
Ride date (Ex:2015/02/25): 2015/3/30<br>
Ride time (24 hour without minutes): 9<br>
Show trains in next x hours: 3<br>
Station number: 1-Taipei, 2-Banqiao, 3-Taoyuan, 4-Hsinchu, 5-Taichung, 6-Chiayi, 7-Tainan, 8-Zuoying<br>
From station number: 2<br>
To station number: 8<br>
 123 |  Banqiao( 9: 2)  ->  Zuoying(10:30) | Travel time:  88mins | Discount: 70%<br>
1627 |  Banqiao( 9:26)  ->  Zuoying(11:18) | Travel time: 112mins | Discount: 50%<br>
 629 |  Banqiao( 9:44)  ->  Zuoying(11:36) | Travel time: 112mins | Discount: 50%<br>
 131 |  Banqiao(10: 2)  ->  Zuoying(11:30) | Travel time:  88mins | Discount: 70%<br>
 633 |  Banqiao(10: 8)  ->  Zuoying(12: 0) | Travel time: 112mins | Discount: 70%<br>
