package edu.usna.mobileos.presidentslist

import android.net.http.SslError
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.webkit.SslErrorHandler
import android.webkit.WebView
import android.webkit.WebViewClient

class WebviewActivity : AppCompatActivity() {


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_webview)

        var president = intent.getStringExtra("president")

        val webView : WebView = findViewById(R.id.wiki_webview)

        president = president?.replace(' ', '_')

        val fullURL : String = "https://en.wikipedia.org/wiki/$president"
        webView.webViewClient = USNAWebViewClient()
        webView.loadUrl(fullURL)

    }


}


private class USNAWebViewClient : WebViewClient(){
    override fun onReceivedSslError(view : WebView?, handler: SslErrorHandler?, error:SslError?){
        Log.e("IT472", "SSL that we dont care about: ${error.toString()}")
        handler?.proceed()
    }
}