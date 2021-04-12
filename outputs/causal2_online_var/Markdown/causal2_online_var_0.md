
# Parameters

    Name :                      causal2_online_var-0
    Main :                      graphTrain
    Level :                     Levels.Causal2
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Epsilon cap :               0.2
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              10
    Topn :                      7
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      27220613486 function calls (26479538629 primitive calls) in 42911.86 seconds

##    Ordered by: cumulative time
   List reduced from 462 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42911.858 42911.858 {built-in method builtins.exec}
                      1    0.001    0.001 42911.858 42911.858 <string>:1(<module>)
                      1  208.736  208.736 42911.857 42911.857 allGraphsTrain.py:5(graphTrain)
                 941382 6620.915    0.007 16047.114    0.017 allGraphs.py:238(transformNot)
              941389928 10543.295    0.000 10543.295    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 941382   20.670    0.000 10012.936    0.011 allGraphsTrain.py:24(<listcomp>)
               95079683 2303.900    0.000 9992.314    0.000 allGraphs.py:198(states)
              847244200 7438.601    0.000 7438.601    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 941382    2.902    0.000 4963.642    0.005 game.py:41(step)
                 941382    3.997    0.000 4778.037    0.005 layers.py:710(step)
                 941382  804.299    0.001 3609.557    0.004 allGraphsTrain.py:30(<listcomp>)
                 941383  122.770    0.000 2906.544    0.003 layers.py:676(update)
               14688942   68.317    0.000 2805.258    0.000 allGraphs.py:245(getInterventions)
                 941382  160.469    0.000 2474.178    0.003 allGraphsTrain.py:32(<listcomp>)
                 941382    2.922    0.000 1891.185    0.002 agent.py:29(learn)
                 941382   18.110    0.000 1886.378    0.002 agent.py:117(_learn)
                 941382   54.763    0.000 1868.269    0.002 learner.py:42(Qlearn)
                 941382   63.036    0.000 1862.580    0.002 layers.py:17(step)
               23382856 1841.540    0.000 1841.540    0.000 {built-in method tensor}
                5133022   35.499    0.000 1793.336    0.000 layers.py:731(restart)
               94138200  139.580    0.000 1790.852    0.000 layer.py:98(move)
               19395853    9.939    0.000 1721.308    0.000 game.py:37(board)
               99786492  218.669    0.000 1521.280    0.000 tensor.py:21(wrapped)
               14097992   11.151    0.000 1444.621    0.000 allGraphs.py:225(rightIntervention)
                 941382   65.628    0.000 1443.859    0.002 allGraphsTrain.py:39(<listcomp>)
                5133022   16.993    0.000 1437.397    0.000 level.py:8(__init__)
        158695530/14097992   97.771    0.000 1381.401    0.000 {built-in method builtins.min}
               39998862   15.950    0.000 1359.037    0.000 allGraphs.py:226(<lambda>)
        303293068/39998862  414.279    0.000 1343.088    0.000 allGraphs.py:61(expected_moves)
                5133022   51.942    0.000 1263.606    0.000 levels.py:151(generate)
               24635112  206.341    0.000 1156.465    0.000 level.py:41(notUsed)
        407891744/93536654  111.381    0.000 1128.931    0.000 allGraphs.py:65(<genexpr>)
               98845110 1041.029    0.000 1041.029    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               94138200  178.126    0.000 1040.840    0.000 layers.py:727(check)
               94138200  963.643    0.000  963.643    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             4183831552  639.786    0.000  944.101    0.000 enum.py:646(__hash__)
                 941382  503.334    0.001  885.684    0.001 agent.py:67(modify)
                 941382    5.044    0.000  744.411    0.001 grad_mode.py:23(decorate_context)
        21651786/2824146   76.393    0.000  737.229    0.000 module.py:715(_call_impl)
                 941382   24.835    0.000  729.836    0.001 adam.py:55(step)
                1882764    4.296    0.000  673.988    0.000 network.py:24(forward)
                1882764   17.834    0.000  658.992    0.000 container.py:115(forward)
                 941382  133.731    0.000  597.940    0.001 functional.py:53(adam)
               24635112   16.042    0.000  547.257    0.000 level.py:38(elementsIn)
               94138200  132.518    0.000  480.632    0.000 layers.py:721(isFree)
                6589681  271.836    0.000  453.092    0.000 layer.py:167(NoRock_update)
              258454173  130.749    0.000  451.529    0.000 {built-in method builtins.any}
                 941382    5.024    0.000  434.107    0.000 tensor.py:181(backward)
              159286480   89.546    0.000  431.061    0.000 allGraphs.py:70(layers_not_in)
                 941382    3.143    0.000  429.083    0.000 __init__.py:68(backward)
                 941382  406.257    0.000  406.257    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 941382   10.236    0.000  389.780    0.000 agent.py:112(__call__)
               24635112  174.903    0.000  351.857    0.000 level.py:39(<listcomp>)
              646041276  274.055    0.000  348.114    0.000 layer.py:95(isFree)
              159286480  170.062    0.000  341.515    0.000 allGraphs.py:71(<listcomp>)
               35931154   24.693    0.000  308.775    0.000 layer.py:69(restart)
               97903728  305.677    0.000  305.677    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2824146   10.339    0.000  305.346    0.000 tensor.py:576(__iter__)
             4183834653  304.315    0.000  304.315    0.000 {built-in method builtins.hash}
                2824146  288.585    0.000  288.585    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              193924792   52.552    0.000  279.391    0.000 {built-in method builtins.all}
                3765528    5.976    0.000  263.629    0.000 conv.py:422(forward)
                3765528    7.140    0.000  255.307    0.000 conv.py:414(_conv_forward)
              163800602   76.819    0.000  252.536    0.000 overrides.py:1070(has_torch_function)
               94138200  154.506    0.000  249.520    0.000 layers.py:225(check)
                3765528  246.886    0.000  246.886    0.000 {built-in method conv2d}
                5133122  125.569    0.000  245.731    0.000 layers.py:30(reset)
               94138200  147.498    0.000  236.617    0.000 layers.py:201(check)
             1182803156  236.041    0.000  236.041    0.000 level.py:32(inverse)
               94138200  147.457    0.000  235.072    0.000 layers.py:213(check)
              712042224  178.217    0.000  219.544    0.000 layers.py:692(<genexpr>)
              303293068  145.071    0.000  211.326    0.000 allGraphs.py:46(p)
              222282212   49.668    0.000  204.101    0.000 layers.py:682(<genexpr>)
                3765528    8.240    0.000  195.011    0.000 linear.py:92(forward)
               52717446  115.813    0.000  191.359    0.000 tensor.py:933(grad)
                3765528   14.014    0.000  183.012    0.000 functional.py:1669(linear)
             1071654314  182.647    0.000  182.647    0.000 enum.py:352(<genexpr>)
               24635112  111.840    0.000  179.358    0.000 {built-in method _functools.reduce}
                 941382   15.904    0.000  164.975    0.000 optimizer.py:167(zero_grad)
             1696389291  150.266    0.000  150.266    0.000 layer.py:91(positions)
               94138300   98.009    0.000  149.645    0.000 layers.py:107(isDone)
                5133022   71.700    0.000  145.746    0.000 level.py:16(<dictcomp>)
                 941382    6.684    0.000  136.771    0.000 agent.py:59(modify_board)
              279801685   98.086    0.000  134.216    0.000 layer.py:130(add)
                 941382   76.273    0.000  130.709    0.000 collector.py:46(collect)
                3765528  129.690    0.000  129.690    0.000 {built-in method addmm}
               15062112  120.441    0.000  120.441    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               94138200   74.553    0.000  115.580    0.000 layers.py:190(check)
              567666582  113.763    0.000  113.763    0.000 layer.py:146(elements)
              431153224   84.766    0.000  100.640    0.000 overrides.py:1083(<genexpr>)
               15062112   99.729    0.000   99.729    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 941382   63.660    0.000   94.567    0.000 allGraphsTrain.py:38(<listcomp>)
                 941382   90.087    0.000   90.087    0.000 {built-in method torch._C._nn.one_hot}
                5648292    4.720    0.000   86.995    0.000 activation.py:713(forward)
                5648292    7.368    0.000   82.275    0.000 functional.py:1292(leaky_relu)
                 941382   20.007    0.000   75.355    0.000 allGraphs.py:229(transform)
                5648292   74.172    0.000   74.172    0.000 {built-in method torch._C._nn.leaky_relu}
                7531056   69.934    0.000   69.934    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              927147290   69.299    0.000   69.299    0.000 {method 'append' of 'list' objects}
              862228920   67.518    0.000   67.518    0.000 level.py:39(<lambda>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9509261: <causal2_online_var_0> in cluster <dcc> Done

Job <causal2_online_var_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Apr 12 00:14:17 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 12 00:14:19 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 00:14:19 2021
Terminated at Mon Apr 12 12:09:40 2021
Results reported at Mon Apr 12 12:09:40 2021

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

    CPU time :                                   42802.67 sec.
    Max Memory :                                 2086 MB
    Average Memory :                             2080.01 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14298.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42922 sec.
    Turnaround time :                            42923 sec.

The output (if any) is above this job summary.

