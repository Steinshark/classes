package edu.usna.mobileos.sampleviews

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    val tag = "IT472"

    // ill get this to you
    lateinit var textView : TextView
    lateinit var editText : EditText
    lateinit var button   : Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // inflate 'activity main' XML
        setContentView(R.layout.activity_main)

        // find it now
        this.textView = findViewById(R.id.testView)
        this.editText = findViewById(R.id.textBox)
        this.button   = findViewById(R.id.button)
        this.button.setOnClickListener {
            this.textView.text = this.editText.text
        }
        // output log message

    }
}


