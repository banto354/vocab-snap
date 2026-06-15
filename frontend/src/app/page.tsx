// トップページ。MVP段階ではアプリ名と説明だけを表示する
// 撮影・登録UIはT07以降で本実装するため、ここでは雛形動作確認に留める
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-4 p-8">
      <h1 className="text-4xl font-bold">パッタン</h1>
      <p className="text-base text-gray-600 dark:text-gray-400">
        写真から英単語を登録する単語帳
      </p>
    </main>
  );
}