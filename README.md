# Othello-Simulation
<a href="https://othellonia.com/">オセロゲーム</a>のダメージ計算をシミュレーションするシステムを作成していく。<br><br>

<h3>フレームワーク</h3>
Docker<br>
Django<br><br>

<h3>開発背景</h3>
このゲームはターン制であり、相手のHPを先にゼロにした方が勝ちなので、与えられるダメージを的確に計算できた方がなにかと有利。<br>
特にこのようなとき<br>
<ul>
  <li>今のターンで飛ばせる(相手のHPをゼロにできる) → アタッカーを出して勝ち</li><br>
  <li>今のターンでは飛ばせない → 防御できる駒を置く</li>
</ul>

ダメージ計算を間違えることで、本来なら今のターンで勝てたのにアタッカーを出さなかったことで逆に負けてしまったり、防御しないと負けてしまう場面でアタッカーを出してしまう事態が頻繫に起こる。<br>
何かと悔しいのでシミュレーションシステムを作成することにした。<br><br>

<h3>仕様</h3>
自分の場合、基本的に「神殴りデッキ」「速攻竜デッキ」しか使わないのでこのデッキを使用することを前提としておく。<br><br>

<h3>現在の進捗状況</h3>
3月から開始しているので殆ど完成していない。<br>
