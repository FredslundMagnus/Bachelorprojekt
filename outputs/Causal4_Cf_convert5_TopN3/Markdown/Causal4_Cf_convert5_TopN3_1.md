
# Parameters

    Name :                      Causal4_Cf_convert5_TopN3-1
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
    Cf convert :                5
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      69145074834 function calls (68841820023 primitive calls) in 86114.07 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.067 86114.067 {built-in method builtins.exec}
                      1    3.922    3.922 86114.067 86114.067 <string>:1(<module>)
                      1  349.505  349.505 86110.145 86110.145 main.py:79(CFagent)
                9880386   35.696    0.000 29723.806    0.003 agent.py:29(learn)
                9880386  735.123    0.000 24858.247    0.003 learner.py:42(Qlearn)
                3293462   15.987    0.000 19246.227    0.006 game.py:41(step)
                3293462   19.668    0.000 18431.704    0.006 layers.py:718(step)
        339502420/36249300 1408.776    0.000 12465.747    0.000 module.py:866(_call_impl)
                3293462  293.985    0.000 12307.642    0.004 layers.py:17(step)
              328985557  884.857    0.000 11986.448    0.000 layer.py:98(move)
               26368914   73.759    0.000 11674.867    0.000 network.py:27(forward)
                3293462  327.710    0.000 11444.389    0.003 agent.py:54(_learn)
               26368914  371.706    0.000 11434.071    0.000 container.py:117(forward)
                3293462  325.201    0.000 10615.508    0.003 agent.py:202(_learn)
                9880386   92.330    0.000 10467.846    0.001 optimizer.py:84(wrapper)
                9880386   42.768    0.000 10049.045    0.001 grad_mode.py:24(decorate_context)
                3293462  934.868    0.000 9988.043    0.003 agent.py:210(counterfact)
                9880386  292.060    0.000 9915.394    0.001 adam.py:55(step)
                9880386 2022.955    0.000 9298.850    0.001 _functional.py:53(adam)
                3293462   94.708    0.000 7607.771    0.002 agent.py:117(_learn)
              328985557 1481.471    0.000 7454.430    0.000 layers.py:735(check)
                9880386   55.296    0.000 6349.674    0.001 tensor.py:195(backward)
                9880386   39.320    0.000 6292.892    0.001 __init__.py:68(backward)
                3293463  462.928    0.000 6077.235    0.002 layers.py:684(update)
                9880386 6035.584    0.001 6035.584    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3293462 4885.478    0.001 5969.851    0.002 replaybuffer.py:67(sample_data)
                3293462 4860.954    0.001 5957.184    0.002 replaybuffer.py:22(sample_data)
                8237068  200.104    0.000 5907.965    0.001 agent.py:49(__call__)
               51969767 5487.786    0.000 5487.786    0.000 {built-in method tensor}
               44386238   30.162    0.000 5270.423    0.000 game.py:37(board)
                3293462 1878.557    0.001 4223.699    0.001 agent.py:88(interveen)
               52737828  116.310    0.000 4109.872    0.000 conv.py:398(forward)
               65869250 2285.629    0.000 3986.249    0.000 layer.py:151(update)
               52737828   81.452    0.000 3938.932    0.000 conv.py:390(_conv_forward)
               52737828 3857.481    0.000 3857.481    0.000 {built-in method conv2d}
                3293462 1945.600    0.001 3647.120    0.001 replaybuffer.py:28(teleporter_save_data)
               72519818  147.281    0.000 3311.234    0.000 linear.py:93(forward)
               72519818   58.480    0.000 3092.010    0.000 functional.py:1737(linear)
              328985557  607.861    0.000 3051.787    0.000 layers.py:729(isFree)
               72519818 3018.904    0.000 3018.904    0.000 {built-in method torch._C._nn.linear}
                3293462 1876.624    0.001 2839.662    0.001 agent.py:67(modify)
                1664536   39.893    0.000 2456.975    0.001 agent.py:175(choose_action)
             2868555554 2020.443    0.000 2443.926    0.000 layer.py:95(isFree)
              184433872 1905.731    0.000 1905.731    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               44465150 1889.712    0.000 1889.712    0.000 {built-in method cat}
               98888732   80.463    0.000 1831.065    0.000 activation.py:713(forward)
               98888732   80.730    0.000 1750.602    0.000 functional.py:1364(leaky_relu)
              126285959 1682.377    0.000 1682.377    0.000 {built-in method clone}
               11530530   84.478    0.000 1676.512    0.000 agent.py:59(modify_board)
              184433872 1664.481    0.000 1664.481    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3293462   55.847    0.000 1653.709    0.001 agent.py:171(__call__)
               98888732 1651.315    0.000 1651.315    0.000 {built-in method torch._C._nn.leaky_relu}
                3293462   53.333    0.000 1547.017    0.000 agent.py:112(__call__)
             6162929649 1067.091    0.000 1491.482    0.000 enum.py:646(__hash__)
                9880386  235.723    0.000 1462.614    0.000 optimizer.py:189(zero_grad)
              329439603  316.718    0.000 1398.440    0.000 {built-in method builtins.any}
                3293462 1049.837    0.000 1358.108    0.000 replaybuffer.py:73(CF_save_data)
              328985557  907.733    0.000 1191.867    0.000 layers.py:77(check)
                3200160   39.109    0.000 1131.468    0.000 layers.py:740(restart)
             3587607540  897.794    0.000 1081.723    0.000 layers.py:700(<genexpr>)
               92216936 1077.773    0.000 1077.773    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              328985557  694.868    0.000 1072.838    0.000 layers.py:286(check)
               11530530 1064.663    0.000 1064.663    0.000 {built-in method torch._C._nn.one_hot}
             1070604593  953.129    0.000  953.129    0.000 layer.py:146(elements)
              328985557  587.590    0.000  948.292    0.000 layers.py:246(check)
               92216936  887.154    0.000  887.154    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3293462   69.418    0.000  865.855    0.000 replaybuffer.py:18(stacker)
               92216936  861.985    0.000  861.985    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3293462   72.155    0.000  858.783    0.000 replaybuffer.py:63(stacker)
               92216936  850.950    0.000  850.950    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              329346300  153.481    0.000  834.315    0.000 {built-in method builtins.all}
                3200160   18.637    0.000  804.889    0.000 level.py:8(__init__)
             1843766605  445.600    0.000  717.459    0.000 layers.py:690(<genexpr>)
             7994942630  682.049    0.000  682.049    0.000 layer.py:91(positions)
                3293462  406.058    0.000  675.373    0.000 collector.py:46(collect)
               92216936  667.563    0.000  667.563    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              328985557  503.563    0.000  644.870    0.000 layers.py:62(check)
                3200160  102.670    0.000  633.271    0.000 levels.py:199(generate)
        8729706354/8729706351  550.576    0.000  618.047    0.000 {built-in method builtins.len}
                8237068  220.542    0.000  608.473    0.000 exploration.py:53(softmaxer)
              328985557  359.527    0.000  551.092    0.000 layers.py:313(check)
              645518636  437.465    0.000  542.749    0.000 tensor.py:906(grad)
              328985557  323.659    0.000  506.994    0.000 layers.py:273(check)
               12987244  188.302    0.000  491.400    0.000 random.py:315(sample)
                9880386   14.525    0.000  481.118    0.000 loss.py:527(forward)
                9880386   36.934    0.000  466.594    0.000 functional.py:2898(mse_loss)
                6400320   50.452    0.000  431.503    0.000 level.py:41(notUsed)
              141109951  430.002    0.000  430.002    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             6162967200  424.399    0.000  424.399    0.000 {built-in method builtins.hash}
              328985557  286.004    0.000  420.696    0.000 layers.py:48(check)
                1664536  373.704    0.000  398.165    0.000 agent.py:186(convert_values)
              328985557  231.038    0.000  337.807    0.000 layers.py:23(check)
               52737828   43.953    0.000  311.058    0.000 flatten.py:39(forward)
                9880386  308.130    0.000  308.130    0.000 {built-in method torch._C._nn.mse_loss}
               19760772  286.017    0.000  286.017    0.000 {built-in method sum}
                6586926  281.199    0.000  281.199    0.000 {built-in method nonzero}
               32001600   40.471    0.000  277.344    0.000 layer.py:69(restart)
             3632095712  273.841    0.000  273.841    0.000 {method 'random' of '_random.Random' objects}
                9881538  270.087    0.000  270.087    0.000 {built-in method max}
              277438494  197.888    0.000  269.660    0.000 layer.py:126(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551822: <Causal4_Cf_convert5_TopN3_1> in cluster <dcc> Done

Job <Causal4_Cf_convert5_TopN3_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:32 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr 23 06:58:57 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 06:58:57 2021
Terminated at Sat Apr 24 06:54:17 2021
Results reported at Sat Apr 24 06:54:17 2021

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

    CPU time :                                   86101.39 sec.
    Max Memory :                                 3441 MB
    Average Memory :                             3410.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12943.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86121 sec.
    Turnaround time :                            272025 sec.

The output (if any) is above this job summary.

