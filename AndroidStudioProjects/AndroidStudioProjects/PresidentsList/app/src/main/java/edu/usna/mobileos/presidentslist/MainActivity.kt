package edu.usna.mobileos.presidentslist

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.Gravity
import android.widget.Toast
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity(), PresidentListener {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val presidentsListView : RecyclerView = findViewById(R.id.presidents_list)

        val data = resources.getStringArray(R.array.presidents)

        val presidentsListAdapter : PresidentsAdapter = PresidentsAdapter(data, this)

        presidentsListView.adapter = presidentsListAdapter
    }

    override fun onItemClick(president: String)     {
        Log.i("IT472",president)
        val a = Toast.makeText(baseContext, president,Toast.LENGTH_SHORT)
        a.setGravity(Gravity.TOP,0,0)
        a.show()

        val intent = Intent(baseContext, WebviewActivity::class.java)
        intent.putExtra("president",president)

        startActivity(intent)
    }
}