
# Parameters

    Name :                      SuperLevel1_teleport-1
    Main :                      teleport
    Level :                     Levels.SuperLevel
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
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      94377750885 function calls (94153956926 primitive calls) in 86114.26 seconds

##    Ordered by: cumulative time
   List reduced from 488 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.262 86114.262 {built-in method builtins.exec}
                      1    1.578    1.578 86114.262 86114.262 <string>:1(<module>)
                      1  278.354  278.354 86112.684 86112.684 main.py:45(teleport)
                4005488   25.379    0.000 35495.381    0.009 game.py:41(step)
                4005488   30.253    0.000 34192.940    0.009 layers.py:718(step)
                4005488  443.340    0.000 25391.312    0.006 layers.py:17(step)
                8010976   44.603    0.000 25384.578    0.003 agent.py:29(learn)
              400548800 1585.405    0.000 24909.393    0.000 layer.py:98(move)
                8010976  619.356    0.000 21060.368    0.003 learner.py:42(Qlearn)
              400548800 2719.823    0.000 16982.016    0.000 layers.py:735(check)
                4005488  170.573    0.000 15228.459    0.004 agent.py:54(_learn)
        251788499/27995551 1110.198    0.000 10511.782    0.000 module.py:715(_call_impl)
                4005488  140.992    0.000 10091.506    0.003 agent.py:117(_learn)
               19984575   55.592    0.000 9729.256    0.000 network.py:27(forward)
               19984575  266.398    0.000 9525.714    0.000 container.py:115(forward)
                4005489  631.987    0.000 8723.408    0.002 layers.py:684(update)
                8010976   66.744    0.000 8049.312    0.001 grad_mode.py:23(decorate_context)
                8010976  300.519    0.000 7862.352    0.001 adam.py:55(step)
                4005488 5723.772    0.001 7693.181    0.002 replaybuffer.py:22(sample_data)
                7968111  254.039    0.000 6570.300    0.001 agent.py:49(__call__)
                8010976 1457.058    0.000 6419.483    0.001 functional.py:53(adam)
              400548800 1004.270    0.000 5311.072    0.000 layers.py:729(isFree)
                4005488 2206.526    0.001 5288.299    0.001 agent.py:88(interveen)
                8010976   55.436    0.000 5212.708    0.001 tensor.py:181(backward)
                8010976   41.382    0.000 5157.272    0.001 __init__.py:68(backward)
                8010976 4889.042    0.001 4889.042    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               52071357 2538.392    0.000 4338.553    0.000 layer.py:151(update)
                4005488 2157.824    0.001 4337.964    0.001 agent.py:67(modify)
             4319677517 3537.467    0.000 4306.801    0.000 layer.py:95(isFree)
                4005488 2270.272    0.001 4104.031    0.001 replaybuffer.py:28(teleporter_save_data)
              400548800 2932.523    0.000 4013.179    0.000 layers.py:471(check)
               39969150   80.205    0.000 3604.468    0.000 conv.py:422(forward)
               39969150   96.720    0.000 3489.123    0.000 conv.py:414(_conv_forward)
               39969150 3376.315    0.000 3376.315    0.000 {built-in method conv2d}
            11784899851 2209.033    0.000 3170.814    0.000 enum.py:646(__hash__)
             1121544085  799.577    0.000 3046.915    0.000 {built-in method builtins.any}
               51942749  121.205    0.000 3000.786    0.000 linear.py:92(forward)
               51942749  209.510    0.000 2815.201    0.000 functional.py:1669(linear)
              400548800 1770.213    0.000 2491.060    0.000 layers.py:77(check)
               11973599  115.282    0.000 2076.775    0.000 agent.py:59(modify_board)
              504691542 1224.424    0.000 2010.119    0.000 tensor.py:933(grad)
                4005488   78.089    0.000 2006.145    0.001 agent.py:112(__call__)
               51942749 2002.368    0.000 2002.368    0.000 {built-in method addmm}
               32001039 1942.438    0.000 1942.438    0.000 {built-in method cat}
               17157256 1916.360    0.000 1916.360    0.000 {built-in method tensor}
             5555275824 1497.830    0.000 1840.715    0.000 layers.py:700(<genexpr>)
                8010976  165.919    0.000 1731.141    0.000 optimizer.py:167(zero_grad)
                4005488   81.425    0.000 1609.889    0.000 replaybuffer.py:18(stacker)
                8010976   15.530    0.000 1604.104    0.000 game.py:37(board)
              128895466 1519.748    0.000 1519.748    0.000 {built-in method clone}
            13386812967 1433.455    0.000 1433.455    0.000 layer.py:91(positions)
              400548800  923.165    0.000 1402.314    0.000 layers.py:246(check)
               11973599 1339.815    0.000 1339.815    0.000 {built-in method torch._C._nn.one_hot}
              400548800  812.775    0.000 1304.829    0.000 layers.py:286(check)
               71927324   76.488    0.000 1295.453    0.000 activation.py:713(forward)
              144197568 1285.460    0.000 1285.460    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               71927324  109.556    0.000 1218.965    0.000 functional.py:1292(leaky_relu)
             1191551447 1195.517    0.000 1195.517    0.000 layer.py:146(elements)
               28041598  167.160    0.000 1172.192    0.000 tensor.py:21(wrapped)
               71927324 1099.389    0.000 1099.389    0.000 {built-in method torch._C._nn.leaky_relu}
              656773967  357.513    0.000 1078.838    0.000 overrides.py:1070(has_torch_function)
              144197568 1044.242    0.000 1044.242    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
            11784929050  961.787    0.000  961.787    0.000 {built-in method builtins.hash}
                3743484   61.140    0.000  848.835    0.000 layers.py:740(restart)
                4005488  439.537    0.000  764.381    0.000 collector.py:46(collect)
               72098784  735.106    0.000  735.106    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              400548800  467.341    0.000  726.552    0.000 layers.py:273(check)
              400548800  466.015    0.000  724.330    0.000 layers.py:141(check)
                7968111  244.872    0.000  723.101    0.000 exploration.py:53(softmaxer)
              400548800  511.880    0.000  716.534    0.000 layers.py:62(check)
               72098784  712.677    0.000  712.677    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              400548800  416.536    0.000  656.832    0.000 layers.py:313(check)
              400548800  431.469    0.000  646.879    0.000 layers.py:124(check)
               72098784  615.207    0.000  615.207    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              400548800  394.531    0.000  591.785    0.000 layers.py:48(check)
               72098784  545.348    0.000  545.348    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        6279249452/6279249450  418.711    0.000  541.727    0.000 {built-in method builtins.len}
                8010976   19.543    0.000  525.481    0.000 loss.py:445(forward)
                8010976   65.870    0.000  505.938    0.000 functional.py:2637(mse_loss)
             5622919140  481.045    0.000  481.045    0.000 {method 'random' of '_random.Random' objects}
              400548800  321.863    0.000  465.996    0.000 layers.py:23(check)
              140869065  446.501    0.000  446.501    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               20027440  417.007    0.000  417.007    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              428590498   89.431    0.000  402.402    0.000 {built-in method builtins.all}
             1393531485  324.534    0.000  400.102    0.000 overrides.py:1083(<genexpr>)
               72098784  399.922    0.000  399.922    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3743484   26.341    0.000  387.226    0.000 level.py:8(__init__)
               48665292   58.417    0.000  384.559    0.000 layer.py:69(restart)
             3327077286  381.226    0.000  381.226    0.000 layer.py:203(isBlocking)
              544274535  266.607    0.000  364.462    0.000 layer.py:130(add)
               51942749  363.898    0.000  363.898    0.000 {method 't' of 'torch._C._TensorBase' objects}
                4005488  135.851    0.000  352.020    0.000 random.py:315(sample)
                4007080  349.155    0.000  349.155    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
              801125062  170.690    0.000  342.923    0.000 layers.py:690(<genexpr>)
              343397108  224.916    0.000  335.540    0.000 layer.py:126(remove)
               24032928  326.748    0.000  326.748    0.000 {built-in method sum}
             4761664992  305.988    0.000  305.988    0.000 layer.py:84(isDead)
                8010976  288.155    0.000  288.155    0.000 {built-in method torch._C._nn.mse_loss}
                4005488   23.396    0.000  270.088    0.000 exploration.py:47(epsilonGreedy)
              801097600  258.293    0.000  258.293    0.000 {method 'union' of 'set' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550909: <SuperLevel1_teleport_1> in cluster <dcc> Done

Job <SuperLevel1_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:50 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 24 07:16:36 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 07:16:36 2021
Terminated at Sun Apr 25 07:11:57 2021
Results reported at Sun Apr 25 07:11:57 2021

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

    CPU time :                                   85896.59 sec.
    Max Memory :                                 2678 MB
    Average Memory :                             2673.31 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13706.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86163 sec.
    Turnaround time :                            399007 sec.

The output (if any) is above this job summary.

