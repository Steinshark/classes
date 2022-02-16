package edu.usna.mobileos.mykitkat

import android.content.res.Configuration
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.util.Log.ASSERT
import android.widget.Button
import android.widget.TextView



class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // This is where all the buttons and textViews are created
        // Additionally, the listeners are added here as well
        if(resources.configuration.orientation == Configuration.ORIENTATION_PORTRAIT){
            // Init the Portrait TextViews and Buttons
            var output_object : TextView  = findViewById(R.id.output)

            var b0_object : Button  = findViewById(R.id.b0)
            var b1_object : Button  = findViewById(R.id.b1)
            var b2_object : Button  = findViewById(R.id.b2)
            var b3_object : Button  = findViewById(R.id.b3)
            var b4_object : Button  = findViewById(R.id.b4)
            var b5_object : Button  = findViewById(R.id.b5)
            var b6_object : Button  = findViewById(R.id.b6)
            var b7_object : Button  = findViewById(R.id.b7)
            var b8_object : Button  = findViewById(R.id.b8)
            var b9_object : Button  = findViewById(R.id.b9)

            var mod_object : Button  = findViewById(R.id.mod)
            var div_object : Button  = findViewById(R.id.div)
            var mul_object : Button  = findViewById(R.id.mul)
            var sub_object : Button  = findViewById(R.id.sub)
            var add_object : Button  = findViewById(R.id.add)

            var AC_object : Button  = findViewById(R.id.AC)
            var plusMinus_object : Button  = findViewById(R.id.plusMinus)
            var dot_object : Button  = findViewById(R.id.dot)
            var eq_object : Button  = findViewById(R.id.eq)


            // Now add the listeners
            b0_object.setOnClickListener{ output_object.text = "${output_object.text}0"}
            b1_object.setOnClickListener{ output_object.text = "${output_object.text}1"}
            b2_object.setOnClickListener{ output_object.text = "${output_object.text}2"}
            b3_object.setOnClickListener{ output_object.text = "${output_object.text}3"}
            b4_object.setOnClickListener{ output_object.text = "${output_object.text}4"}
            b5_object.setOnClickListener{ output_object.text = "${output_object.text}5"}
            b6_object.setOnClickListener{ output_object.text = "${output_object.text}6"}
            b7_object.setOnClickListener{ output_object.text = "${output_object.text}7"}
            b8_object.setOnClickListener{ output_object.text = "${output_object.text}8"}
            b9_object.setOnClickListener{ output_object.text = "${output_object.text}9"}

            // op listeners
            mod_object.setOnClickListener{ output_object.text = "${output_object.text}%"}
            div_object.setOnClickListener{ output_object.text = "${output_object.text}/"}
            mul_object.setOnClickListener{ output_object.text = "${output_object.text}x"}
            sub_object.setOnClickListener{ output_object.text = "${output_object.text}-"}
            add_object.setOnClickListener{ output_object.text = "${output_object.text}+"}
            dot_object.setOnClickListener{ output_object.text = "${output_object.text}."}

            // pot pourri listeners
            AC_object.setOnClickListener{ output_object.text = ""}
            plusMinus_object.setOnClickListener{ output_object.text = "${output_object.text}#"}
            dot_object.setOnClickListener{ output_object.text = "${output_object.text}."}
            eq_object.setOnClickListener{ output_object.text = ""}
        }

        else {
            // Init the Landscape TextViews and Buttons
            var outputText_object : TextView = findViewById(R.id.outputText)

            var b0_norm_object : Button = findViewById(R.id.b0_norm)
            var b1_norm_object : Button = findViewById(R.id.b1_norm)
            var b2_norm_object : Button = findViewById(R.id.b2_norm)
            var b3_norm_object : Button = findViewById(R.id.b3_norm)
            var b4_norm_object : Button = findViewById(R.id.b4_norm)
            var b5_norm_object : Button = findViewById(R.id.b5_norm)
            var b6_norm_object : Button = findViewById(R.id.b6_norm)
            var b7_norm_object : Button = findViewById(R.id.b7_norm)
            var b8_norm_object : Button = findViewById(R.id.b8_norm)
            var b9_norm_object : Button = findViewById(R.id.b9_norm)

            var mod_norm_object : Button = findViewById(R.id.mod_norm)
            var div_norm_object : Button = findViewById(R.id.div_norm)
            var mul_norm_object : Button = findViewById(R.id.mul_norm)
            var sub_norm_object : Button = findViewById(R.id.sub_norm)
            var add_norm_object : Button = findViewById(R.id.add_norm)
            var dot_norm_object : Button = findViewById(R.id.dot_norm)

            var lPer_object : Button = findViewById(R.id.lPer)
            var rPer_object : Button = findViewById(R.id.rPer)
            var mc_object : Button = findViewById(R.id.mc)
            var mp_object : Button = findViewById(R.id.mp)
            var mm_object : Button = findViewById(R.id.mm)
            var mr_object : Button = findViewById(R.id.mr)
            var AC_norm_object : Button = findViewById(R.id.AC_norm)
            var plusMinus_norm_object : Button = findViewById(R.id.plusMinus_norm)
            var twoND_object : Button = findViewById(R.id.twoND)
            var xSquare_object : Button = findViewById(R.id.xSquare)
            var xCube_object : Button = findViewById(R.id.xCube)
            var xToY_object : Button = findViewById(R.id.xToY)
            var eToX_object : Button = findViewById(R.id.eToX)
            var tenToX_object : Button = findViewById(R.id.tenToX)
            var xReciprocal_object : Button = findViewById(R.id.xReciprocal)
            var XSqrt_object : Button = findViewById(R.id.XSqrt)
            var xCubeRoot_object : Button = findViewById(R.id.xCubeRoot)
            var xSqrtY_object : Button = findViewById(R.id.xSqrtY)
            var ln_object : Button = findViewById(R.id.ln)
            var log10_object : Button = findViewById(R.id.log10)
            var xFactorial_object : Button = findViewById(R.id.xFactorial)
            var sin_object : Button = findViewById(R.id.sin)
            var cos_object : Button = findViewById(R.id.cos)
            var tan_object : Button = findViewById(R.id.tan)
            var e_object : Button = findViewById(R.id.e)
            var EE_object : Button = findViewById(R.id.EE)
            var Rad_object : Button = findViewById(R.id.Rad)
            var sinh_object : Button = findViewById(R.id.sinh)
            var cosh_object : Button = findViewById(R.id.cosh)
            var tanh_object : Button = findViewById(R.id.tanh)
            var pi_object : Button = findViewById(R.id.pi)
            var Rand_object : Button = findViewById(R.id.Rand)

            var eq_norm_object : Button = findViewById(R.id.eq_norm)
            eq_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}="}

            // Now add the listeners
            b7_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}7"}
            b8_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}8"}
            b9_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}9"}
            b4_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}4"}
            b5_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}5"}
            b6_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}6"}
            b1_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}1"}
            b2_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}2"}
            b3_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}3"}

            // op listeners
            mod_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}%"}
            div_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}/"}
            mul_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}x"}
            sub_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}-"}
            add_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}+"}
            dot_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}."}

            // pot pourri listeners
            lPer_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}("}
            rPer_object.setOnClickListener{ outputText_object.text = "${outputText_object.text})"}
            mc_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            mp_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            mm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            mr_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            AC_norm_object.setOnClickListener{ outputText_object.text = ""}
            plusMinus_norm_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            twoND_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            xSquare_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            xCube_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            xToY_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            eToX_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            tenToX_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            xReciprocal_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            XSqrt_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            xCubeRoot_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            xSqrtY_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            ln_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}ln"}
            log10_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}log"}
            xFactorial_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            sin_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}sin("}
            cos_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}cos("}
            tan_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}tan("}
            e_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            EE_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            Rad_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
            sinh_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}sinh("}
            cosh_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}cosh("}
            tanh_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}tanh("}
            pi_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}pi"}
            Rand_object.setOnClickListener{ outputText_object.text = "${outputText_object.text}#"}
        }



    }
}
