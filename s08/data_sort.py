raw_data = """[[1530851700,6489.99,6516.7,6490,6510.3,18.601353019999998],[1530851400,6481.05,6490,6488.34,6490,11.858941159999997],[1530851100,6488.33,6496.03,6496.03,6488.33,10.606287119999998],[1530850800,6488,6500.09,6500.09,6496.03,35.651085560000006],[1530850500,6491,6511.23,6511.22,6500.08,29.627860240000008],[1530850200,6503.81,6524.01,6524.01,6511.23,46.19016329000001],[1530849900,6524,6525.49,6525.17,6524.01,8.203854750000001],[1530849600,6525.16,6525.17,6525.16,6525.17,7.181878229999999],[1530849300,6525.16,6530.03,6530.03,6525.17,9.23780811],[1530849000,6530.02,6530.99,6530.98,6530.03,11.33994162],[1530848700,6530.98,6530.99,6530.99,6530.99,8.16668383],[1530848400,6530.98,6530.99,6530.98,6530.99,5.640960660000001],[1530848100,6530.98,6530.99,6530.99,6530.98,4.2866578],[1530847800,6530.98,6530.99,6530.99,6530.99,3.1036804599999996],[1530847500,6529.99,6530.99,6530,6530.99,3.560029039999999],[1530847200,6529.99,6530,6530,6530,2.66214482],[1530846900,6528.2,6532.97,6532.97,6530,4.26713245],[1530846600,6532.96,6532.97,6532.96,6532.97,2.80403866],[1530846300,6532.96,6539.99,6539.97,6532.96,10.632501350000004],[1530846000,6539.95,6539.98,6539.96,6539.96,4.0120003099999995],[1530845700,6536,6539.96,6537.03,6539.95,4.12497281],[1530845400,6535.05,6539.95,6538.44,6537.22,12.59321345],[1530845100,6535.54,6539,6535.55,6538.44,9.28849929],[1530844800,6530.6,6538.39,6535.57,6535.55,3.0617075199999997],[1530844500,6528.95,6539.74,6535.43,6535.57,3.3411310700000003],[1530844200,6529.61,6539.99,6539.98,6535.43,12.081684439999997],[1530843900,6529.97,6539.99,6529.97,6539.98,19.412346479999993],[1530843600,6525,6529.99,6529.99,6529.94,15.46071421],[1530843300,6529.47,6529.99,6529.48,6529.99,9.913139390000001],[1530843000,6525.1,6529.48,6529.47,6529.48,8.557130599999999],[1530842700,6525,6529.48,6529.48,6529.47,4.576025489999999],[1530842400,6516,6529.48,6516.01,6529.47,14.65051995],[1530842100,6516,6518.63,6518.63,6516.01,9.278414199999999],[1530841800,6516.66,6523.44,6523.44,6518.62,26.44562026],[1530841500,6515.17,6523.45,6523.45,6523.43,4.96852238],[1530841200,6521.99,6525,6521.99,6523.45,14.796354430000001],[1530840900,6521.99,6522,6521.99,6521.99,14.266547290000002],[1530840600,6521.99,6522,6522,6522,4.329445600000001],[1530840300,6521.99,6522,6522,6522,17.02822967],[1530840000,6521.99,6522,6522,6522,3.7774766699999995],[1530839700,6515.01,6522,6515.02,6522,45.22496247000001],[1530839400,6510.8,6522,6515.41,6515.02,8.057779239999999],[1530839100,6511.13,6524.37,6524.37,6515.66,18.327765819999996],[1530838800,6524.37,6533.46,6533.46,6524.37,23.14973294000001],[1530838500,6533.45,6533.46,6533.46,6533.46,10.01368003],[1530838200,6530.09,6533.46,6530.1,6533.46,29.696122229999993],[1530837900,6529.99,6530.1,6530,6530.1,6.38170971],[1530837600,6526.92,6530,6529.42,6529.99,15.009505470000002],[1530837300,6525.48,6533.46,6533.46,6529.43,11.20789959],[1530837000,6533.45,6538.45,6538.45,6533.46,5.767991970000001],[1530836700,6533.38,6539.52,6533.39,6538.45,16.151761949999997],[1530836400,6533.38,6533.39,6533.39,6533.39,6.0651890999999996],[1530836100,6533.38,6535.84,6535.84,6533.38,11.903593180000001],[1530835800,6533.38,6539.89,6533.39,6535.85,9.7808518],[1530835500,6528,6544.94,6528.01,6533.39,16.66095999],[1530835200,6528,6532.96,6532.96,6528.01,6.15932539],[1530834900,6532.95,6532.96,6532.95,6532.95,6.85193608],[1530834600,6530,6541.92,6541.92,6532.96,14.550554569999997],[1530834300,6540,6544.93,6544.93,6541.91,9.66572835],[1530834000,6536.48,6548,6536.48,6544.93,17.806465749999997],[1530833700,6536.48,6536.49,6536.49,6536.48,17.189428630000002],[1530833400,6532.04,6536.49,6533,6536.48,21.142055020000008],[1530833100,6529.99,6533,6530,6533,5.268018619999999],[1530832800,6528,6530,6528.01,6530,10.96706161],[1530832500,6526.15,6536.57,6531,6528,9.525737419999999],[1530832200,6525,6532.04,6532.04,6530.99,3.63135239],[1530831900,6529.06,6538.5,6535.9,6532.04,7.33594493],[1530831600,6529.06,6538.5,6538.35,6535.9,17.77462577],[1530831300,6531.99,6538.35,6532,6538.34,6.910610959999999],[1530831000,6526.23,6537.35,6529.5,6531.99,7.55867007],[1530830700,6522.99,6529.5,6522.99,6529.5,13.844294409999998],[1530830400,6515.84,6534.39,6534.39,6523,7.1802363499999995],[1530830100,6499.97,6540,6499.97,6540,81.60462404000003],[1530829800,6494.35,6499.98,6494.36,6499.98,10.765381489999996],[1530829500,6488.7,6494.36,6488.7,6494.35,11.745079380000004],[1530829200,6487.23,6488.69,6487.23,6488.69,24.350115859999995],[1530828900,6480.76,6487.24,6487.23,6487.24,13.464921030000003],[1530828600,6487.23,6488.31,6488.3,6487.24,24.17147186],[1530828300,6488.3,6488.31,6488.3,6488.31,9.64136381],[1530828000,6488.3,6488.31,6488.31,6488.31,7.50610429],[1530827700,6488.3,6488.31,6488.31,6488.31,5.37645098],[1530827400,6486.36,6494.19,6490.72,6488.31,40.73933533],[1530827100,6484.13,6494.36,6489.17,6490.72,26.333741590000017],[1530826800,6489.17,6494.36,6492.72,6489.18,8.031742430000001],[1530826500,6488.11,6496,6491.48,6492.73,10.65421107],[1530826200,6489.37,6497.07,6497.07,6491.48,7.4567048499999995],[1530825900,6493.49,6497.07,6493.49,6497.07,6.39283002],[1530825600,6476.44,6493.5,6476.45,6493.5,34.028167530000005],[1530825300,6475.47,6487.87,6487.86,6476.45,15.535643580000011],[1530825000,6485.77,6499.22,6494.36,6487.86,44.25597024],[1530824700,6491,6504.61,6500.67,6495.11,9.286801230000002],[1530824400,6500.66,6504.61,6504.61,6500.67,4.31964993],[1530824100,6504,6504.61,6504.61,6504.6,13.32033673],[1530823800,6500.83,6504.78,6504.77,6504.6,14.185637810000001],[1530823500,6491.9,6504.78,6491.9,6504.77,11.21370262],[1530823200,6491.1,6500.06,6500.06,6491.89,9.72596513],[1530822900,6500.05,6500.39,6500.09,6500.06,5.689103619999999],[1530822600,6491.01,6508.49,6500.01,6500.08,13.391021739999998],[1530822300,6498.91,6503.21,6498.91,6500.01,12.155827489999998],[1530822000,6495,6510.99,6503.49,6498.9,12.234912449999998],[1530821700,6486.85,6503.49,6486.85,6503.49,12.33885915],[1530821400,6486.85,6492.78,6491.01,6486.86,5.33051362],[1530821100,6490,6500.02,6500.01,6491.01,9.809003439999998],[1530820800,6500,6515.35,6504.22,6500.02,21.56982146],[1530820500,6493.6,6527.86,6493.61,6505,112.86427533999998],[1530820200,6483.93,6499.88,6483.93,6493.6,80.79603644999997],[1530819900,6481.74,6484.88,6484.87,6483.94,6.98063261],[1530819600,6478.99,6484.88,6478.99,6484.88,32.824901370000006],[1530819300,6465.01,6479,6467.43,6478.99,30.46253325],[1530819000,6462.07,6469.99,6469.99,6467.44,54.04127526999997],[1530818700,6469.98,6474,6473.99,6469.98,28.019989690000003],[1530818400,6469.98,6474,6469.98,6473.99,38.86786755000004],[1530818100,6465,6469.99,6468,6469.99,53.714613269999724],[1530817800,6467,6469.99,6469.98,6468.01,16.550697940000063],[1530817500,6465.05,6469.99,6466.9,6469.99,14.494759259999991],[1530817200,6461,6479.98,6479.98,6466.89,55.02868779000002],[1530816900,6472.22,6484.88,6472.23,6479.98,40.418256140000004],[1530816600,6461.01,6476.68,6461.01,6472.24,12.991456759999997],[1530816300,6460.63,6475,6475,6461.01,19.187319759999998],[1530816000,6473.51,6489.53,6489.53,6473.52,18.85820980999999],[1530815700,6449.5,6489.99,6449.51,6489.53,110.17991810000002],[1530815400,6449.5,6557.54,6557.54,6449.5,499.92710352000006],[1530815100,6550,6567.79,6567.79,6557.55,23.698271029999994],[1530814800,6562.5,6567.79,6563.54,6567.78,31.545508610000002],[1530814500,6563.53,6573.58,6573.58,6563.54,16.974400019999994],[1530814200,6563.36,6582.23,6582.23,6573.58,47.89507103999999],[1530813900,6555.36,6586.18,6555.37,6582.23,63.52034495999999],[1530813600,6550,6566.46,6566.45,6555.37,32.42757682],[1530813300,6557.53,6566.46,6557.54,6566.46,17.62950887],[1530813000,6557.53,6570.72,6570.72,6557.53,31.724892819999987],[1530812700,6570.05,6575.82,6570.21,6570.72,11.66812552999999],[1530812400,6564.69,6573.68,6564.7,6570.21,4.62903036],[1530812100,6564.69,6572.91,6572.9,6564.7,8.720201479999998],[1530811800,6563.77,6572.9,6568.28,6572.9,13.528777350000002],[1530811500,6551,6575,6559.1,6568.28,28.175670939999993],[1530811200,6559.09,6567.29,6567.29,6559.1,10.162051599999998],[1530810900,6567.28,6578.42,6578.41,6567.28,14.789152890000008],[1530810600,6575.05,6578.42,6575.05,6578.42,4.1413122699999985],[1530810300,6570,6583.01,6583.01,6575.06,14.869369899999997],[1530810000,6583,6596.04,6589.79,6583.01,18.399606199999997],[1530809700,6584.12,6607.01,6607,6589.79,14.582126039999999],[1530809400,6600.27,6609.16,6600.29,6607.01,32.026092679999984],[1530809100,6600.28,6615.17,6615.16,6600.29,16.263973429999993],[1530808800,6606.83,6618.44,6609.61,6615.17,46.241122239999996],[1530808500,6606.99,6613.26,6606.99,6609.6,6.303343619999998],[1530808200,6606,6611.48,6606.8,6606.99,13.251121239999996],[1530807900,6605.38,6620.05,6620.04,6606.79,42.952138870000056],[1530807600,6620.03,6622,6621.99,6620.04,8.258832039999996],[1530807300,6621.99,6624.44,6622,6622,11.587395569999996],[1530807000,6610.42,6623.01,6623,6622,25.989067920000004],[1530806700,6621.15,6631.11,6621.16,6623,19.73550611999999],[1530806400,6605.37,6639.34,6609.29,6621.16,54.37268751000016],[1530806100,6602.4,6616,6608.85,6609.28,25.674575709999996],[1530805800,6593.07,6609.3,6597,6608.85,28.194728009999988],[1530805500,6590.01,6599.09,6593.85,6596.99,10.427852569999999],[1530805200,6593.84,6605,6605,6593.85,12.749654770000003],[1530804900,6589.99,6605,6591.71,6605,13.278900469999991],[1530804600,6590,6604,6604,6591.7,16.852518819999997],[1530804300,6573.09,6610.35,6573.1,6603.99,231.86201337000014],[1530804000,6550.01,6572.12,6556.46,6572.12,46.240392610000015],[1530803700,6539,6576.28,6576.28,6556.46,76.73831066999998],[1530803400,6573.23,6582.38,6582.38,6576.28,10.466756389999992],[1530803100,6575.11,6584.6,6575.11,6581.94,22.69202865000003],[1530802800,6569.99,6584.42,6584.42,6575.12,26.753725109999987],[1530802500,6584.41,6584.42,6584.41,6584.42,9.681588319999998],[1530802200,6583.11,6591.52,6591.51,6584.42,16.895080489999998],[1530801900,6581.68,6595.89,6588.08,6591.52,34.73194107000002],[1530801600,6588.08,6597,6597,6588.09,6.384196799999999],[1530801300,6597,6598.38,6597,6597.01,10.346055119999999],[1530801000,6597,6597.01,6597.01,6597,15.061384500000004],[1530800700,6597,6605,6601.31,6597,5.914417579999999],[1530800400,6572.05,6612.52,6587.59,6601.37,43.2450952],[1530800100,6583,6591.84,6591.84,6587.59,18.17195731],[1530799800,6569.98,6593.28,6576.1,6591.84,30.344047350000007],[1530799500,6568,6603.75,6603.74,6576.1,66.37849799000003],[1530799200,6585,6603.75,6599,6603.74,45.292036290000006],[1530798900,6586.18,6604.59,6587.77,6599.01,25.81970881],[1530798600,6585,6603.39,6603.38,6587.77,37.178436399999995],[1530798300,6597,6615,6612.5,6603.39,24.639026569999995],[1530798000,6593.98,6620,6620,6612.5,47.80007854000001],[1530797700,6615.7,6631.01,6631.01,6620,8.09377511],[1530797400,6628.05,6635,6630,6631.01,8.660924399999999],[1530797100,6606.54,6632.33,6632.33,6630,47.86437629999999],[1530796800,6628.25,6634.9,6628.26,6632.32,14.85726458],[1530796500,6628.25,6640,6637.69,6628.25,23.84428529],[1530796200,6636,6649.96,6649.96,6637.7,7.15267636],[1530795900,6641.89,6670,6643.2,6649.97,74.10624891000002],[1530795600,6632.17,6644.87,6633.06,6643.15,35.00745141999998],[1530795300,6632.16,6633.61,6632.16,6633.61,18.292742499999996],[1530795000,6632.15,6649,6635.46,6632.16,13.753132289999996],[1530794700,6633.13,6642.86,6641.39,6635.46,11.7791193],[1530794400,6635.01,6659.61,6641.29,6641.38,30.43817298],[1530794100,6635.55,6645,6640.01,6641.28,10.47658556],[1530793800,6627.77,6645,6627.78,6640.02,11.850221889999997],[1530793500,6627.77,6635,6635,6627.78,12.948228480000001],[1530793200,6627.12,6635,6627.12,6635,4.023277200000001],[1530792900,6624,6627.13,6625,6627.13,5.44474935],[1530792600,6624.13,6625,6624.14,6625,3.17484206],[1530792300,6603.47,6632.38,6603.47,6624.14,14.440207809999995],[1530792000,6575.86,6615.11,6615.11,6603.48,122.74917792999999],[1530791700,6615.1,6624.79,6624.79,6615.11,2.7254809100000004],[1530791400,6624.78,6628.97,6627.3,6624.78,36.0148391],[1530791100,6626.64,6634.73,6634.73,6627.29,7.66565923],[1530790800,6620,6635,6628.45,6634.72,5.844255389999999],[1530790500,6628.45,6629.17,6628.56,6628.46,4.163672849999999],[1530790200,6622.35,6638.99,6638.99,6628.55,11.064089480000003],[1530789900,6631.2,6638.99,6636.21,6638.98,6.598714290000001],[1530789600,6636.21,6645.93,6645.93,6636.22,2.1560134699999995],[1530789300,6643.27,6653.06,6643.28,6645.94,3.10253976],[1530789000,6639.63,6648.14,6644.82,6643.27,5.185442470000001],[1530788700,6642.28,6684,6642.28,6644.81,117.89692020000001],[1530788400,6634.17,6643.82,6634.17,6642.29,6.590824309999999],[1530788100,6631.49,6650,6647.47,6634.17,4.53120032],[1530787800,6633.33,6648.84,6633.33,6647.73,10.739485009999997],[1530787500,6624.26,6631.23,6630.05,6631.23,2.51367997],[1530787200,6626.25,6636.79,6626.25,6630.06,13.262615929999999],[1530786900,6614.98,6631.76,6614.98,6626.24,12.44741395],[1530786600,6614.98,6614.99,6614.99,6614.99,3.88508305],[1530786300,6609.06,6614.99,6609.07,6614.99,5.984998279999999],[1530786000,6601.95,6610,6601.95,6609.06,4.94221219],[1530785700,6599.88,6609.75,6600.87,6601.95,4.81112633],[1530785400,6600.86,6615.39,6615.39,6600.86,16.98099647],[1530785100,6615.39,6618.05,6618.05,6615.4,5.791596310000001],[1530784800,6612.51,6631.92,6631.92,6618.05,40.54371445000002],[1530784500,6575.27,6650,6581.02,6631.91,95.04892624],[1530784200,6563.09,6585.4,6563.3,6582.33,8.03217419],[1530783900,6546.21,6585.64,6585.64,6562.66,122.09607842],[1530783600,6585.64,6604.41,6604.41,6585.64,14.959388479999996],[1530783300,6604.4,6604.41,6604.41,6604.4,2.11766718],[1530783000,6604.4,6604.41,6604.41,6604.41,1.6371175199999999],[1530782700,6604.4,6610.01,6610.01,6604.41,3.1578968],[1530782400,6610,6615.94,6615.94,6610.01,5.690066250000001],[1530782100,6615.94,6621.96,6621.95,6615.95,0.61613511],[1530781800,6604.58,6623,6607.32,6621.98,10.615699420000004],[1530781500,6602,6612.84,6612,6606.11,3.60786648],[1530781200,6601,6617.5,6617.5,6612,5.61895513],[1530780900,6614.67,6620,6619.99,6617.46,1.14848394],[1530780600,6610.53,6620,6610.53,6620,6.888869689999994],[1530780300,6605.23,6612,6605.23,6610.52,1.54732413],[1530780000,6598.03,6608.71,6598.03,6605.22,5.25457313],[1530779700,6598.03,6605.82,6605.82,6598.03,6.369455590000001],[1530779400,6599.99,6606.24,6599.99,6605.88,0.6930322800000001],[1530779100,6599.99,6607.01,6607.01,6599.99,3.9244620599999998],[1530778800,6607,6611.41,6611.4,6607,2.18212779],[1530778500,6608.52,6611.41,6608.52,6611.4,3.2842862],[1530778200,6606.6,6609.59,6609.47,6609.59,1.51249616],[1530777900,6601.54,6615.83,6601.55,6609.46,11.575286029999997],[1530777600,6598.65,6609.96,6609.96,6601.55,5.981571919999997],[1530777300,6605.3,6609.97,6605.3,6609.97,2.2249375499999977],[1530777000,6605.3,6608.11,6608.1,6605.31,8.16734715],[1530776700,6597.19,6615.49,6597.2,6608.11,43.31005694000001],[1530776400,6593.8,6600.4,6600.4,6597.2,5.016813769999998],[1530776100,6596.02,6604.09,6604.09,6600.4,11.391459509999994],[1530775800,6604.08,6604.1,6604.09,6604.08,12.73335878000001],[1530775500,6593.5,6604.15,6593.51,6604.08,13.154239839999997],[1530775200,6592.66,6615.83,6604.26,6597.84,38.19940108999997],[1530774900,6601.85,6605.3,6605.3,6604.26,1.2690069300000002],[1530774600,6602.19,6605.3,6602.2,6605.3,5.25111732],[1530774300,6597.49,6602.44,6597.49,6602.19,5.64914332],[1530774000,6592.66,6597.5,6592.67,6597.5,1.35052759],[1530773700,6588.26,6597.68,6597.67,6592.67,5.376390690000001],[1530773400,6597.67,6598.89,6598.89,6597.67,4.10822039],[1530773100,6588.39,6600,6588.39,6598.88,12.202194610000001],[1530772800,6584.07,6588.4,6584.07,6588.4,6.000519529999999],[1530772500,6582.9,6584.07,6582.91,6584.06,9.929022709999995],[1530772200,6582.9,6592.03,6592.03,6582.91,5.127663050000001],[1530771900,6592.03,6599.99,6599.99,6592.03,2.5847054999999997],[1530771600,6599.99,6600.01,6600.01,6599.99,8.478507749999999],[1530771300,6595.47,6600.01,6600,6599.21,6.513279559999998],[1530771000,6600,6605.3,6605.3,6600,2.798146],[1530770700,6600,6609.71,6609.7,6605.3,9.150716569999998],[1530770400,6603.49,6610,6603.5,6609.71,10.916525660000007],[1530770100,6603.49,6603.5,6603.5,6603.5,0.73544974],[1530769800,6595.47,6611.19,6595.48,6603.5,28.64882385000001],[1530769500,6579.8,6595.48,6579.81,6595.48,8.152142940000038],[1530769200,6569.17,6592.03,6592.03,6579.81,45.991213089999995],[1530768900,6590,6592.03,6592.03,6592.03,12.388744449999999],[1530768600,6592.02,6603.5,6603.5,6592.03,3.91002928],[1530768300,6598.74,6613.49,6613.49,6603.5,10.486342889999994],[1530768000,6610.45,6613.5,6610.46,6613.5,7.884637969999998],[1530767700,6592.02,6630.96,6630.96,6610.45,100.45351926],[1530767400,6628.38,6671.43,6628.38,6630.98,105.85420939000002],[1530767100,6620.01,6628.39,6620.01,6628.39,11.114821829999993],[1530766800,6616.32,6621,6621,6620,8.23900012],[1530766500,6620.99,6621.1,6621.01,6620.99,6.741326259999939],[1530766200,6621,6626.01,6626.01,6621,6.1594861399999425],[1530765900,6620.15,6626.43,6623.8,6626,11.320587640000118],[1530765600,6623.66,6627,6623.67,6623.79,6.104521059999941],[1530765300,6616.4,6630,6623.72,6623.66,19.702833180000187],[1530765000,6616.54,6623.72,6621.51,6623.71,11.934142080000044],[1530764700,6614.99,6626.79,6615.32,6621.5,12.073261990000017],[1530764400,6614.47,6626.8,6626.8,6616.77,29.217606270000555],[1530764100,6625,6637.19,6628.97,6626.79,21.167539239999687],[1530763800,6616.55,6629.93,6616.55,6628.98,13.018439419999892],[1530763500,6616.55,6629.99,6629.99,6616.56,25.74187752000074],[1530763200,6622.68,6632,6627.01,6629.98,14.548218479999854],[1530762900,6614.33,6635.77,6635.76,6627,9.358132769999903],[1530762600,6624.56,6640.67,6628.54,6635.77,19.510642119999797],[1530762300,6620.88,6629.98,6629.97,6628.55,18.528442220000187],[1530762000,6620.84,6629.99,6620.84,6629.98,27.163004239999342]]"""
data = eval(raw_data)
data2 = sorted(data,key=lambda s: s[2] - s[1], reverse=True)
diff_vals = list(map(lambda s: s[2]-s[1], data2))
print(diff_vals[:10])