
# Parameters

    Name :                      Diamonds4_0.0_NN-0
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.0
    Use model :                 True
    Depth :                     3
    Model explore :             100000
    Samples :                   5
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Softmax cap :               0.0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12357884427 function calls (11855698470 primitive calls) in 35716.22 seconds

##    Ordered by: cumulative time
   List reduced from 476 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35716.221 35716.221 {built-in method builtins.exec}
                      1    0.001    0.001 35716.221 35716.221 <string>:1(<module>)
                      1   32.157   32.157 35716.220 35716.220 allGraphsTrain.py:13(graphTrain)
                 127685  158.982    0.001 24968.330    0.196 allGraphsTrain.py:40(<listcomp>)
                 905504    4.122    0.000 24803.227    0.027 allGraphs.py:179(getInterventionsmodel)
        42688036/758798 3495.812    0.000 23393.202    0.031 allGraphs.py:186(recursiveBEST)
        507713577/47866477 1687.602    0.000 17162.307    0.000 module.py:715(_call_impl)
               45729340  105.209    0.000 17099.895    0.000 BayesianNN.py:18(forward)
               45984710  582.442    0.000 16783.459    0.000 container.py:115(forward)
               39669744 1833.098    0.000 16724.191    0.000 BayesianNN.py:65(predict_no_convert)
              137698760  248.178    0.000 7556.906    0.000 linear.py:92(forward)
              137698760  468.565    0.000 7200.550    0.000 functional.py:1669(linear)
                 127685 1385.092    0.011 5656.676    0.044 allGraphs.py:156(transformNot)
              137698760 4984.572    0.000 4984.572    0.000 {built-in method addmm}
              137188020  100.526    0.000 3833.682    0.000 dropout.py:57(forward)
                1754082   20.231    0.000 3785.246    0.002 BayesianNN.py:57(learn)
              137188020  410.043    0.000 3733.156    0.000 functional.py:960(dropout)
                1754082   21.258    0.000 3473.008    0.002 BayesianNN.py:21(learn)
              137188020 3218.863    0.000 3218.863    0.000 {built-in method dropout}
              137954130   85.924    0.000 2469.872    0.000 activation.py:713(forward)
                4305514   56.492    0.000 2464.562    0.001 BayesianNN.py:61(predict)
              137954130  142.217    0.000 2383.948    0.000 functional.py:1292(leaky_relu)
              137954130 2226.322    0.000 2226.322    0.000 {built-in method torch._C._nn.leaky_relu}
                 127685    3.579    0.000 1856.428    0.015 allGraphsTrain.py:33(<listcomp>)
               12896286  485.611    0.000 1852.865    0.000 allGraphs.py:114(states)
              129440498 1779.486    0.000 1779.486    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                1881767   10.027    0.000 1634.140    0.001 grad_mode.py:23(decorate_context)
                1881767   45.879    0.000 1604.174    0.001 adam.py:55(step)
              114916900 1490.712    0.000 1490.712    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1881767  289.274    0.000 1374.296    0.001 functional.py:53(adam)
          555910/146706   52.443    0.000 1304.980    0.009 allGraphs.py:202(recursiveExplore)
                 127685    5.012    0.000 1247.979    0.010 allGraphs.py:141(transform)
               55873052  184.438    0.000 1204.388    0.000 tensor.py:21(wrapped)
              137698760 1199.295    0.000 1199.295    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6059596  822.584    0.000 1031.729    0.000 BayesianNN.py:43(convert_data)
               42466127  140.388    0.000  963.023    0.000 tensor.py:506(__rsub__)
                1881767   12.594    0.000  869.188    0.000 tensor.py:181(backward)
                1881767    5.893    0.000  856.594    0.000 __init__.py:68(backward)
               42466127  822.635    0.000  822.635    0.000 {built-in method rsub}
                1881767  804.497    0.000  804.497    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               42338442  684.000    0.000  684.000    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              254786800  174.371    0.000  553.517    0.000 overrides.py:1070(has_torch_function)
                 127685    0.477    0.000  532.430    0.004 game.py:42(step)
                 127685    0.654    0.000  504.658    0.004 layers.py:827(step)
                 127685   34.537    0.000  456.927    0.004 allGraphsTrain.py:44(<listcomp>)
              408836990  178.764    0.000  427.162    0.000 {built-in method builtins.any}
              508096632  407.498    0.000  407.498    0.000 {built-in method torch._C._get_tracing_state}
                 127685    0.427    0.000  343.041    0.003 agent.py:29(learn)
                 127685    2.632    0.000  342.347    0.003 agent.py:117(_learn)
               80821864  213.254    0.000  340.227    0.000 tensor.py:933(grad)
                 127685    9.806    0.000  339.716    0.003 learner.py:42(Qlearn)
                1881767   31.853    0.000  328.408    0.000 optimizer.py:167(zero_grad)
                 127685    9.028    0.000  289.616    0.002 layers.py:17(step)
               23091944  288.416    0.000  288.416    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12768500   19.994    0.000  279.580    0.000 layer.py:106(move)
                 127685   11.957    0.000  268.276    0.002 allGraphsTrain.py:51(<listcomp>)
               23091944  241.365    0.000  241.365    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              671992454  171.988    0.000  216.992    0.000 overrides.py:1083(<genexpr>)
                 127686   17.166    0.000  213.745    0.002 layers.py:793(update)
               13406925  207.179    0.000  207.179    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               59008580  189.983    0.000  189.983    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               12768500  186.714    0.000  186.714    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               12119193  181.337    0.000  181.337    0.000 {built-in method zeros}
                2112199  178.074    0.000  178.074    0.000 {built-in method tensor}
               12768500   38.129    0.000  177.842    0.000 layers.py:844(check)
             2076839018  174.272    0.000  174.272    0.000 {method 'values' of 'collections.OrderedDict' objects}
              324158341  167.680    0.000  167.681    0.000 module.py:765(__getattr__)
               11545972  161.987    0.000  161.987    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1543930    1.580    0.000  158.122    0.000 game.py:38(board)
               46240080   28.400    0.000  157.610    0.000 flatten.py:39(forward)
        1287168129/1287168127  146.782    0.000  149.089    0.000 {built-in method builtins.len}
               11545972  142.127    0.000  142.127    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 127685   73.034    0.001  135.637    0.001 agent.py:67(modify)
               11545972  130.469    0.000  130.469    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               11545972  116.986    0.000  116.986    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 255370    0.670    0.000  111.370    0.000 network.py:28(forward)
                 905504    7.166    0.000  100.551    0.000 allGraphs.py:167(format)
                1881767    2.272    0.000  100.405    0.000 loss.py:445(forward)
                1881767    8.612    0.000   98.133    0.000 functional.py:2637(mse_loss)
               11545972   92.536    0.000   92.536    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               68641652   37.707    0.000   91.843    0.000 {built-in method builtins.all}
              139069787   62.627    0.000   90.471    0.000 _VF.py:25(__getattr__)
               44230628   87.626    0.000   87.626    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 180705    1.534    0.000   76.555    0.000 layers.py:849(restart)
              393972268   72.927    0.000   72.927    0.000 {built-in method builtins.getattr}
              137698760   71.959    0.000   71.959    0.000 functional.py:1686(<listcomp>)
                 127685    1.580    0.000   66.052    0.001 agent.py:112(__call__)
                1881767   65.529    0.000   65.529    0.000 {built-in method torch._C._nn.mse_loss}
               12768500   17.416    0.000   64.150    0.000 layers.py:838(isFree)
                 180705    0.763    0.000   62.975    0.000 level.py:8(__init__)
               70219867   49.818    0.000   62.885    0.000 types.py:171(__get__)
              240233333   42.094    0.000   61.379    0.000 enum.py:646(__hash__)
              138975730   55.214    0.000   55.214    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                 180705    2.031    0.000   51.625    0.000 levels.py:456(generate)
                9015141   51.000    0.000   51.000    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 893802   27.184    0.000   49.322    0.000 layer.py:175(NoRock_update)
                 866926    8.289    0.000   47.527    0.000 level.py:41(notUsed)
               81262960   36.811    0.000   46.734    0.000 layer.py:103(isFree)
                1892186   46.240    0.000   46.240    0.000 {built-in method cat}
                1881767    7.445    0.000   44.419    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651552: <Diamonds4_0.0_NN_0> in cluster <dcc> Done

Job <Diamonds4_0.0_NN_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue May 18 21:12:59 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed May 19 17:04:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 17:04:03 2021
Terminated at Thu May 20 02:59:26 2021
Results reported at Thu May 20 02:59:26 2021

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

    CPU time :                                   35664.99 sec.
    Max Memory :                                 2066 MB
    Average Memory :                             2058.67 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14318.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35776 sec.
    Turnaround time :                            107187 sec.

The output (if any) is above this job summary.

