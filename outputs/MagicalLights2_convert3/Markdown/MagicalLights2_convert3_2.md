
# Parameters

    Name :                      MagicalLights2_convert3-2
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
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
    Topn :                      1
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      58183607386 function calls (57937192307 primitive calls) in 86118.77 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86118.766 86118.766 {built-in method builtins.exec}
                      1    7.432    7.432 86118.766 86118.766 <string>:1(<module>)
                      1  423.114  423.114 86111.334 86111.334 main.py:79(CFagent)
                7538877   50.527    0.000 22707.368    0.003 agent.py:29(learn)
                2512959   17.331    0.000 20258.659    0.008 game.py:41(step)
                2512959   21.963    0.000 19451.994    0.008 layers.py:718(step)
                7538863  631.187    0.000 17963.297    0.002 learner.py:42(Qlearn)
                2512959 1711.764    0.001 11673.545    0.005 agent.py:210(counterfact)
                2512959  260.528    0.000 11660.772    0.005 layers.py:17(step)
              249568354  800.891    0.000 11377.202    0.000 layer.py:98(move)
        275324353/28910965 1354.724    0.000 11260.556    0.000 module.py:866(_call_impl)
               21372102   84.621    0.000 10436.534    0.000 network.py:27(forward)
               21372102  337.996    0.000 10168.534    0.000 container.py:117(forward)
                2512959  403.158    0.000 8831.790    0.004 agent.py:54(_learn)
                2512959  401.010    0.000 7967.229    0.003 agent.py:202(_learn)
                2512960  427.210    0.000 7735.496    0.003 layers.py:684(update)
                2512959 6111.283    0.002 7198.193    0.003 replaybuffer.py:22(sample_data)
                2512959 5967.547    0.002 6988.920    0.003 replaybuffer.py:67(sample_data)
              249568354 1247.189    0.000 6943.555    0.000 layers.py:735(check)
                7538863  108.346    0.000 6618.323    0.001 optimizer.py:84(wrapper)
                7538863   50.526    0.000 6176.813    0.001 grad_mode.py:24(decorate_context)
                7538863  306.922    0.000 6004.628    0.001 adam.py:55(step)
                6915811  297.290    0.000 5920.586    0.001 agent.py:49(__call__)
                2512959  118.357    0.000 5833.982    0.002 agent.py:117(_learn)
                7538863 1246.799    0.000 5392.654    0.001 _functional.py:53(adam)
                2512959 3130.794    0.001 5384.070    0.002 replaybuffer.py:28(teleporter_save_data)
               44654184 5122.339    0.000 5122.339    0.000 {built-in method tensor}
               38790773   33.747    0.000 4954.534    0.000 game.py:37(board)
               50259190 3031.668    0.000 4899.377    0.000 layer.py:151(update)
                7538863   44.677    0.000 4898.899    0.001 tensor.py:195(backward)
                7538863   48.716    0.000 4853.044    0.001 __init__.py:68(backward)
                2512959 2652.158    0.001 4776.968    0.002 agent.py:88(interveen)
                7538863 4577.256    0.001 4577.256    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               42744204  125.717    0.000 3983.172    0.000 conv.py:398(forward)
               42744204   90.603    0.000 3800.874    0.000 conv.py:390(_conv_forward)
               42744204 3710.271    0.000 3710.271    0.000 {built-in method conv2d}
                1891524   55.827    0.000 3117.072    0.002 agent.py:175(choose_action)
              249568354  523.309    0.000 3073.265    0.000 layers.py:729(isFree)
               59090388  137.357    0.000 2859.330    0.000 linear.py:93(forward)
                6743747   86.488    0.000 2651.707    0.000 layers.py:740(restart)
               59090388   59.781    0.000 2648.711    0.000 functional.py:1737(linear)
               59090388 2577.021    0.000 2577.021    0.000 {built-in method torch._C._nn.linear}
             2344766260 2155.523    0.000 2549.956    0.000 layer.py:95(isFree)
                2512959 1569.044    0.001 2450.502    0.001 agent.py:67(modify)
              213218203 2296.906    0.000 2296.906    0.000 {built-in method clone}
                2512959 1469.435    0.001 1973.587    0.001 replaybuffer.py:73(CF_save_data)
                6743747   39.622    0.000 1852.336    0.000 level.py:8(__init__)
               34558290 1758.895    0.000 1758.895    0.000 {built-in method cat}
                9428770   93.530    0.000 1672.857    0.000 agent.py:59(modify_board)
                6743747  258.417    0.000 1493.816    0.000 levels.py:199(generate)
                2512945   65.486    0.000 1489.299    0.001 agent.py:171(__call__)
             5376783766  998.754    0.000 1448.918    0.000 enum.py:646(__hash__)
               80462490   91.432    0.000 1418.345    0.000 activation.py:713(forward)
                2512959   65.029    0.000 1345.664    0.001 agent.py:112(__call__)
               80462490   83.929    0.000 1326.914    0.000 functional.py:1364(leaky_relu)
               80462490 1228.250    0.000 1228.250    0.000 {built-in method torch._C._nn.leaky_relu}
             1435305842 1205.786    0.000 1205.786    0.000 layer.py:146(elements)
              247065213  271.630    0.000 1191.514    0.000 {built-in method builtins.any}
                9428770 1100.203    0.000 1100.203    0.000 {built-in method torch._C._nn.one_hot}
              249568354  844.272    0.000 1087.047    0.000 layers.py:77(check)
              249568354  695.060    0.000 1073.789    0.000 layers.py:246(check)
              140725424 1035.856    0.000 1035.856    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               13487494  116.564    0.000 1000.419    0.000 level.py:41(notUsed)
                7538863  176.362    0.000  956.297    0.000 optimizer.py:189(zero_grad)
              249568354  584.081    0.000  955.115    0.000 layers.py:286(check)
             2690074783  766.866    0.000  919.885    0.000 layers.py:700(<genexpr>)
              140725424  912.047    0.000  912.047    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2512959   63.466    0.000  835.773    0.000 replaybuffer.py:18(stacker)
                2512945   63.531    0.000  777.532    0.000 replaybuffer.py:63(stacker)
               67437470  101.552    0.000  688.972    0.000 layer.py:69(restart)
              249568354  519.761    0.000  666.774    0.000 layers.py:62(check)
              251296000  125.816    0.000  642.217    0.000 {built-in method builtins.all}
                6915811  227.143    0.000  636.810    0.000 exploration.py:53(softmaxer)
               70362712  616.635    0.000  616.635    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               18513412  234.062    0.000  597.616    0.000 random.py:315(sample)
             6069250887  589.736    0.000  589.736    0.000 layer.py:91(positions)
             1302832751  346.515    0.000  548.450    0.000 layers.py:690(<genexpr>)
               70362712  542.094    0.000  542.094    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        6567247018/6567247015  470.229    0.000  537.135    0.000 {built-in method builtins.len}
               70362712  509.356    0.000  509.356    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                1891524  475.841    0.000  507.676    0.000 agent.py:186(convert_values)
               70362712  505.827    0.000  505.827    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              249568354  338.135    0.000  500.444    0.000 layers.py:273(check)
              225159918  491.547    0.000  491.547    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                7538863   18.942    0.000  480.690    0.000 loss.py:527(forward)
                7538863   52.525    0.000  461.748    0.000 functional.py:2898(mse_loss)
              249568354  300.394    0.000  460.865    0.000 layers.py:313(check)
              492539068  366.315    0.000  450.683    0.000 tensor.py:906(grad)
             5376812581  450.170    0.000  450.170    0.000 {built-in method builtins.hash}
              283580461  342.687    0.000  441.224    0.000 layer.py:126(remove)
                2512959  240.010    0.000  417.339    0.000 collector.py:46(collect)
              249568354  289.927    0.000  411.844    0.000 layers.py:48(check)
              670545023  292.746    0.000  397.398    0.000 layer.py:130(add)
              274134138  394.748    0.000  394.748    0.000 level.py:32(inverse)
               13487494   16.427    0.000  384.346    0.000 level.py:38(elementsIn)
               70362712  372.128    0.000  372.128    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6743847  184.675    0.000  369.014    0.000 layers.py:36(reset)
                6743747  166.504    0.000  291.633    0.000 level.py:16(<dictcomp>)
              249568354  197.019    0.000  287.009    0.000 layers.py:23(check)
              366028985  188.282    0.000  282.715    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9571370: <MagicalLights2_convert3_2> in cluster <dcc> Done

Job <MagicalLights2_convert3_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 24 18:36:26 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 24 18:43:24 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 18:43:24 2021
Terminated at Sun Apr 25 18:38:51 2021
Results reported at Sun Apr 25 18:38:51 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
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

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85911.59 sec.
    Max Memory :                                 8102 MB
    Average Memory :                             5873.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8282.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86129 sec.
    Turnaround time :                            86545 sec.

The output (if any) is above this job summary.

