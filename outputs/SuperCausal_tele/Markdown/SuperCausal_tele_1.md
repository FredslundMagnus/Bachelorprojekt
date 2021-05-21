
# Parameters

    Name :                      SuperCausal_tele-1
    Main :                      teleport
    Level :                     Levels.CausalSuper
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      113859823121 function calls (113580622322 primitive calls) in 86113.37 seconds

##    Ordered by: cumulative time
   List reduced from 492 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.366 86113.366 {built-in method builtins.exec}
                      1    1.610    1.610 86113.366 86113.366 <string>:1(<module>)
                      1  221.551  221.551 86111.756 86111.756 main.py:46(teleport)
                4995330   18.865    0.000 30202.022    0.006 game.py:42(step)
                4995330   29.161    0.000 28972.019    0.006 layers.py:827(step)
                9990660   34.930    0.000 28614.798    0.003 agent.py:29(learn)
                9990660  740.866    0.000 24185.370    0.002 learner.py:42(Qlearn)
                4995330  371.679    0.000 20785.483    0.004 layers.py:17(step)
              499533000  774.141    0.000 20374.430    0.000 layer.py:106(move)
                4995330  537.963    0.000 17256.533    0.003 agent.py:54(_learn)
              499533000 2106.783    0.000 15458.773    0.000 layers.py:844(check)
        314122207/34922419 1239.969    0.000 11540.987    0.000 module.py:866(_call_impl)
                4995330  146.957    0.000 11304.800    0.002 agent.py:117(_learn)
               24931759   71.731    0.000 10754.564    0.000 network.py:28(forward)
               24931759  342.985    0.000 10532.997    0.000 container.py:117(forward)
                9990660   88.043    0.000 10177.993    0.001 optimizer.py:84(wrapper)
                9990660   41.745    0.000 9771.217    0.001 grad_mode.py:24(decorate_context)
                9990660  265.004    0.000 9637.207    0.001 adam.py:55(step)
                9990660 1980.935    0.000 9063.755    0.001 _functional.py:53(adam)
                4995331  655.223    0.000 8122.146    0.002 layers.py:793(update)
                9945769  245.734    0.000 7160.340    0.001 agent.py:49(__call__)
                4995330 3356.257    0.001 6853.358    0.001 agent.py:88(interveen)
                4995330 3585.362    0.001 6632.312    0.001 replaybuffer.py:28(teleporter_save_data)
                9990660   42.376    0.000 6006.283    0.001 tensor.py:195(backward)
                9990660   37.087    0.000 5962.465    0.001 __init__.py:68(backward)
                9990660 5701.560    0.001 5701.560    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4995330 3794.497    0.001 5432.341    0.001 replaybuffer.py:22(sample_data)
                4995330 2741.658    0.001 4178.654    0.001 agent.py:67(modify)
            18131433259 2684.937    0.000 3902.168    0.000 enum.py:646(__hash__)
               49863518  110.918    0.000 3882.081    0.000 conv.py:398(forward)
               49863518   63.717    0.000 3721.085    0.000 conv.py:390(_conv_forward)
               49863518 3657.369    0.000 3657.369    0.000 {built-in method conv2d}
              499533000  911.475    0.000 3443.261    0.000 layers.py:838(isFree)
              499533000 1891.457    0.000 3114.453    0.000 layers.py:734(check)
               64804617  133.255    0.000 3009.524    0.000 linear.py:93(forward)
               49953310 1580.686    0.000 2829.633    0.000 layer.py:175(NoRock_update)
               64804617   53.788    0.000 2811.675    0.000 functional.py:1737(linear)
               64804617 2744.838    0.000 2744.838    0.000 {built-in method torch._C._nn.linear}
              499533000 1588.730    0.000 2590.215    0.000 layers.py:700(check)
              202158200 2539.480    0.000 2539.480    0.000 {built-in method clone}
             4885299564 2025.576    0.000 2531.786    0.000 layer.py:103(isFree)
              499533000 1477.468    0.000 2431.434    0.000 layers.py:717(check)
                4995330   73.566    0.000 2267.725    0.000 agent.py:112(__call__)
               14941099   99.865    0.000 2171.056    0.000 agent.py:59(modify_board)
              496974592  470.039    0.000 2039.066    0.000 {built-in method builtins.any}
              179831880 1848.427    0.000 1848.427    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               21317295 1782.951    0.000 1782.951    0.000 {built-in method tensor}
               89736376   76.317    0.000 1690.198    0.000 activation.py:713(forward)
               39917749 1662.761    0.000 1662.761    0.000 {built-in method cat}
              179831880 1637.835    0.000 1637.835    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               89736376   75.294    0.000 1613.882    0.000 functional.py:1364(leaky_relu)
                2558509   30.283    0.000 1609.706    0.001 layers.py:849(restart)
             5466720501 1301.047    0.000 1569.027    0.000 layers.py:809(<genexpr>)
               89736376 1522.819    0.000 1522.819    0.000 {built-in method torch._C._nn.leaky_relu}
            16596084143 1495.262    0.000 1495.262    0.000 layer.py:99(positions)
                9990660   11.199    0.000 1421.983    0.000 game.py:38(board)
                9990660  228.523    0.000 1418.848    0.000 optimizer.py:189(zero_grad)
                2558509   13.970    0.000 1391.024    0.001 level.py:8(__init__)
               14941099 1387.459    0.000 1387.459    0.000 {built-in method torch._C._nn.one_hot}
              499533000  831.559    0.000 1312.710    0.000 layers.py:686(check)
                4995330   84.382    0.000 1286.357    0.000 replaybuffer.py:18(stacker)
                2558509   43.483    0.000 1233.618    0.000 levels.py:261(generate)
            18131469586 1217.237    0.000 1217.237    0.000 {built-in method builtins.hash}
              499533000  761.731    0.000 1216.161    0.000 layers.py:658(check)
              499533000  753.721    0.000 1201.241    0.000 layers.py:672(check)
               21004652  189.889    0.000 1143.700    0.000 level.py:41(notUsed)
               89915940 1015.508    0.000 1015.508    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4995330  611.024    0.000 1014.641    0.000 collector.py:46(collect)
               89915940  870.612    0.000  870.612    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               89915940  845.925    0.000  845.925    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               89915940  837.352    0.000  837.352    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              499533100  149.382    0.000  805.040    0.000 {built-in method builtins.all}
                9945769  272.533    0.000  751.893    0.000 exploration.py:53(softmaxer)
             1193442658  722.466    0.000  722.466    0.000 layer.py:154(elements)
             1781532877  416.749    0.000  712.271    0.000 layers.py:799(<genexpr>)
              217099299  678.543    0.000  678.543    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               89915940  650.379    0.000  650.379    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              499533000  372.184    0.000  571.111    0.000 layers.py:646(check)
        7456730870/7456730868  495.772    0.000  569.536    0.000 {built-in method builtins.len}
               21004652   15.897    0.000  551.061    0.000 level.py:38(elementsIn)
              629411634  410.884    0.000  511.467    0.000 tensor.py:906(grad)
                9990660   13.675    0.000  491.245    0.000 loss.py:527(forward)
                9990660   37.427    0.000  477.570    0.000 functional.py:2898(mse_loss)
              499533000  324.007    0.000  475.367    0.000 layers.py:23(check)
               29971980  430.735    0.000  430.735    0.000 {built-in method sum}
             4885299564  427.230    0.000  427.230    0.000 layer.py:211(isBlocking)
             5517767893  400.462    0.000  400.462    0.000 {method 'random' of '_random.Random' objects}
               21004652  176.488    0.000  358.257    0.000 level.py:39(<listcomp>)
                4995330  122.519    0.000  342.020    0.000 random.py:315(sample)
                9990660  315.048    0.000  315.048    0.000 {built-in method torch._C._nn.mse_loss}
              449347594  205.269    0.000  305.823    0.000 layer.py:134(remove)
              547397922  216.304    0.000  298.857    0.000 layer.py:138(add)
               49863518   32.206    0.000  290.872    0.000 flatten.py:39(forward)
                9992153  279.153    0.000  279.153    0.000 {built-in method max}
             4969745910  267.980    0.000  267.980    0.000 layer.py:92(isDead)
                4995330   20.889    0.000  264.888    0.000 exploration.py:47(epsilonGreedy)
               49863518  258.666    0.000  258.666    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                9945769  242.631    0.000  242.631    0.000 {built-in method multinomial}
              974301708  237.952    0.000  237.952    0.000 level.py:32(inverse)
                9990660  219.188    0.000  219.188    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9672990: <SuperCausal_tele_1> in cluster <dcc> Done

Job <SuperCausal_tele_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May 20 18:43:26 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May 20 18:43:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May 20 18:43:28 2021
Terminated at Fri May 21 18:38:54 2021
Results reported at Fri May 21 18:38:54 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85893.38 sec.
    Max Memory :                                 9327 MB
    Average Memory :                             6031.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7057.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86170 sec.
    Turnaround time :                            86128 sec.

The output (if any) is above this job summary.

