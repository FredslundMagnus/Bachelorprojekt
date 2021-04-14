
# Parameters

    Name :                      ReTest3-0
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        500000.0
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      32463414570 function calls (32317372175 primitive calls) in 42914.00 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42913.998 42913.998 {built-in method builtins.exec}
                      1    3.465    3.465 42913.998 42913.998 <string>:1(<module>)
                      1  193.539  193.539 42910.533 42910.533 main.py:75(CFagent)
                5461689   19.624    0.000 16262.973    0.003 agent.py:29(learn)
                5459139  405.020    0.000 13531.588    0.002 learner.py:42(Qlearn)
                1820563    9.518    0.000 8721.104    0.005 game.py:41(step)
                1820563   12.657    0.000 8299.962    0.005 layers.py:718(step)
                1820563  192.170    0.000 6283.819    0.003 agent.py:54(_learn)
        164276756/18236052  677.366    0.000 6101.627    0.000 module.py:866(_call_impl)
                1820563  189.200    0.000 5813.221    0.003 agent.py:202(_learn)
                5459139   48.634    0.000 5706.586    0.001 optimizer.py:84(wrapper)
               12776913   35.613    0.000 5685.530    0.000 network.py:24(forward)
               12776913  176.500    0.000 5566.715    0.000 container.py:117(forward)
                5459139   24.336    0.000 5481.766    0.001 grad_mode.py:24(decorate_context)
                5459139  164.423    0.000 5404.773    0.001 adam.py:55(step)
                1820563  154.224    0.000 5194.979    0.003 layers.py:17(step)
                5459139 1117.811    0.000 5065.806    0.001 _functional.py:53(adam)
              181805209  289.623    0.000 5025.542    0.000 layer.py:98(move)
                1820563   52.263    0.000 4134.350    0.002 agent.py:117(_learn)
                5459139   22.433    0.000 3401.953    0.001 tensor.py:195(backward)
                5459139   21.654    0.000 3378.694    0.001 __init__.py:68(backward)
                5459139 3235.902    0.001 3235.902    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1820564  261.662    0.000 3076.372    0.002 layers.py:684(update)
                1820563  424.967    0.000 3067.235    0.002 agent.py:210(counterfact)
              181805209  634.567    0.000 2946.006    0.000 layers.py:735(check)
                1820563 1543.935    0.001 2880.915    0.002 replaybuffer.py:28(teleporter_save_data)
                1820563 1481.048    0.001 2801.766    0.002 agent.py:88(interveen)
                3658224   97.558    0.000 2670.897    0.001 agent.py:49(__call__)
                1820563 2070.895    0.001 2663.021    0.001 replaybuffer.py:22(sample_data)
                1820563 1661.243    0.001 2233.854    0.001 replaybuffer.py:52(sample_data)
               24498531 2181.038    0.000 2181.038    0.000 {built-in method tensor}
               20324004   12.445    0.000 2056.722    0.000 game.py:37(board)
               25553826   55.709    0.000 2026.456    0.000 conv.py:398(forward)
               25553826   36.271    0.000 1943.480    0.000 conv.py:390(_conv_forward)
               25553826 1907.209    0.000 1907.209    0.000 {built-in method conv2d}
               29129016  974.753    0.000 1732.137    0.000 layer.py:167(NoRock_update)
               34689613   71.827    0.000 1604.588    0.000 linear.py:93(forward)
                1820563 1063.950    0.001 1592.254    0.001 agent.py:67(modify)
              181805209  270.170    0.000 1527.266    0.000 layers.py:729(isFree)
               34689613   28.756    0.000 1495.015    0.000 functional.py:1737(linear)
               34689613 1459.017    0.000 1459.017    0.000 {built-in method torch._C._nn.linear}
               98657306 1262.217    0.000 1262.217    0.000 {built-in method clone}
             1268801534 1050.829    0.000 1257.096    0.000 layer.py:95(isFree)
              101900528 1030.133    0.000 1030.133    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               23671667  980.470    0.000  980.470    0.000 {built-in method cat}
                1818013   32.283    0.000  918.473    0.001 agent.py:171(__call__)
              101900528  905.789    0.000  905.789    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               47466526   38.706    0.000  884.501    0.000 activation.py:713(forward)
                1820563   31.520    0.000  867.890    0.000 agent.py:112(__call__)
               47466526   39.396    0.000  845.795    0.000 functional.py:1364(leaky_relu)
                1820563  611.989    0.000  803.616    0.000 replaybuffer.py:58(CF_save_data)
               47466526  798.343    0.000  798.343    0.000 {built-in method torch._C._nn.leaky_relu}
                5478787   36.391    0.000  793.339    0.000 agent.py:59(modify_board)
                5459139  127.403    0.000  785.425    0.000 optimizer.py:189(zero_grad)
             2746862350  481.747    0.000  681.842    0.000 enum.py:646(__hash__)
              181791666  153.532    0.000  647.608    0.000 {built-in method builtins.any}
                2085298   21.918    0.000  641.129    0.000 layers.py:740(restart)
              181805209  391.956    0.000  616.229    0.000 layers.py:286(check)
               50950264  566.690    0.000  566.690    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              182056400   65.427    0.000  554.802    0.000 {built-in method builtins.all}
              181805209  329.541    0.000  550.091    0.000 layers.py:246(check)
              737228109  182.535    0.000  511.483    0.000 layers.py:690(<genexpr>)
                5478787  509.238    0.000  509.238    0.000 {built-in method torch._C._nn.one_hot}
               50950264  496.545    0.000  496.545    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1619739918  405.556    0.000  494.076    0.000 layers.py:700(<genexpr>)
               50950264  470.086    0.000  470.086    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               50950264  463.538    0.000  463.538    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                1820563   33.434    0.000  463.270    0.000 replaybuffer.py:18(stacker)
                2085298   11.070    0.000  448.899    0.000 level.py:8(__init__)
                1818013   30.767    0.000  448.811    0.000 replaybuffer.py:48(stacker)
              597617322  433.563    0.000  433.563    0.000 layer.py:146(elements)
                1820563  224.255    0.000  371.443    0.000 collector.py:46(collect)
               50950264  359.371    0.000  359.371    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2085298   42.352    0.000  353.233    0.000 levels.py:164(generate)
              105954106  317.519    0.000  317.519    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             3544299612  310.425    0.000  310.425    0.000 layer.py:91(positions)
              182056400  200.705    0.000  303.857    0.000 layers.py:113(isDone)
              181805209  193.002    0.000  301.819    0.000 layers.py:273(check)
        4039978084/4039978081  261.371    0.000  296.893    0.000 {built-in method builtins.len}
              356651932  231.046    0.000  286.810    0.000 tensor.py:906(grad)
                7811722  107.094    0.000  284.694    0.000 random.py:315(sample)
                3658224  100.970    0.000  282.618    0.000 exploration.py:53(softmaxer)
              181805209  176.302    0.000  279.420    0.000 layers.py:313(check)
                1820563   48.042    0.000  265.762    0.000 agent.py:277(counterfact_check)
                5459139    8.362    0.000  263.672    0.000 loss.py:527(forward)
                4170596   37.341    0.000  256.425    0.000 level.py:41(notUsed)
                5459139   20.457    0.000  255.310    0.000 functional.py:2898(mse_loss)
              181805209  161.333    0.000  238.490    0.000 layers.py:48(check)
             2746883437  200.098    0.000  200.098    0.000 {built-in method builtins.hash}
              181805209  129.628    0.000  187.185    0.000 layers.py:23(check)
               12743941  182.479    0.000  182.479    0.000 {built-in method sum}
                5459139  167.175    0.000  167.175    0.000 {built-in method torch._C._nn.mse_loss}
               16682384   20.679    0.000  164.852    0.000 layer.py:69(restart)
                5459686  151.677    0.000  151.677    0.000 {built-in method max}
               25553826   18.301    0.000  150.422    0.000 flatten.py:39(forward)
              270385714  109.165    0.000  150.283    0.000 layer.py:130(add)
                3641128  143.461    0.000  143.461    0.000 {built-in method nonzero}
              233852181   97.537    0.000  142.820    0.000 random.py:250(_randbelow_with_getrandbits)
              164443285   91.417    0.000  135.896    0.000 layer.py:126(remove)
               25553826  132.121    0.000  132.121    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9512494: <ReTest3_0> in cluster <dcc> Done

Job <ReTest3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 13 13:40:47 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 13 20:42:20 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 20:42:20 2021
Terminated at Wed Apr 14 08:37:41 2021
Results reported at Wed Apr 14 08:37:41 2021

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

    CPU time :                                   42800.69 sec.
    Max Memory :                                 6752 MB
    Average Memory :                             5059.15 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9632.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42922 sec.
    Turnaround time :                            68214 sec.

The output (if any) is above this job summary.

