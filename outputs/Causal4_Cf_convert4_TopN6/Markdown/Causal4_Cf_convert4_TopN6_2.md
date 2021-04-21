
# Parameters

    Name :                      Causal4_Cf_convert4_TopN6-2
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
    Cf convert :                4
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      69567193232 function calls (69267147321 primitive calls) in 86114.37 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.368 86114.368 {built-in method builtins.exec}
                      1    4.506    4.506 86114.368 86114.368 <string>:1(<module>)
                      1  361.582  361.582 86109.862 86109.862 main.py:79(CFagent)
                9724680   35.390    0.000 29324.371    0.003 agent.py:29(learn)
                9724674  738.493    0.000 24405.114    0.003 learner.py:42(Qlearn)
                3241560   14.064    0.000 19298.534    0.006 game.py:41(step)
                3241560   18.818    0.000 18490.165    0.006 layers.py:718(step)
        335853099/35808879 1356.900    0.000 12464.857    0.000 module.py:866(_call_impl)
                3241560  263.690    0.000 12044.511    0.004 layers.py:17(step)
              323908690  858.733    0.000 11754.545    0.000 layer.py:98(move)
               26084205   70.835    0.000 11694.586    0.000 network.py:27(forward)
               26084205  363.804    0.000 11459.957    0.000 container.py:117(forward)
                3241560  355.540    0.000 11324.015    0.003 agent.py:54(_learn)
                3241560  352.688    0.000 10480.719    0.003 agent.py:202(_learn)
                9724674   82.737    0.000 10371.597    0.001 optimizer.py:84(wrapper)
                3241560  919.737    0.000 10131.980    0.003 agent.py:210(counterfact)
                9724674   40.419    0.000 9973.776    0.001 grad_mode.py:24(decorate_context)
                9724674  282.916    0.000 9844.542    0.001 adam.py:55(step)
                9724674 2027.656    0.000 9250.692    0.001 _functional.py:53(adam)
                3241560  100.764    0.000 7461.709    0.002 agent.py:117(_learn)
              323908690 1385.853    0.000 7317.584    0.000 layers.py:735(check)
                3241561  456.912    0.000 6400.700    0.002 layers.py:684(update)
                9724674   40.377    0.000 6048.540    0.001 tensor.py:195(backward)
                9724674   39.226    0.000 6006.676    0.001 __init__.py:68(backward)
                8176204  227.888    0.000 5953.980    0.001 agent.py:49(__call__)
                9724674 5750.939    0.001 5750.939    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3241560 4562.782    0.001 5679.953    0.002 replaybuffer.py:22(sample_data)
                3241560 4480.830    0.001 5566.568    0.002 replaybuffer.py:67(sample_data)
               51163593 5429.377    0.000 5429.377    0.000 {built-in method tensor}
               43693030   28.407    0.000 5210.948    0.000 game.py:37(board)
                3241560 2172.090    0.001 4525.074    0.001 agent.py:88(interveen)
                3241560 2287.765    0.001 4268.444    0.001 replaybuffer.py:28(teleporter_save_data)
               52168410  112.227    0.000 4145.907    0.000 conv.py:398(forward)
               52168410   72.966    0.000 3980.563    0.000 conv.py:390(_conv_forward)
               64831210 2314.770    0.000 3953.252    0.000 layer.py:151(update)
               52168410 3907.597    0.000 3907.597    0.000 {built-in method conv2d}
               71769495  143.903    0.000 3346.353    0.000 linear.py:93(forward)
               71769495   60.004    0.000 3128.744    0.000 functional.py:1737(linear)
               71769495 3053.557    0.000 3053.557    0.000 {built-in method torch._C._nn.linear}
              323908690  571.290    0.000 2994.951    0.000 layers.py:729(isFree)
                3241560 1871.112    0.001 2821.555    0.001 agent.py:67(modify)
                1700213   39.627    0.000 2672.986    0.002 agent.py:175(choose_action)
             2810993167 2004.466    0.000 2423.661    0.000 layer.py:95(isFree)
               43833334 1928.512    0.000 1928.512    0.000 {built-in method cat}
              181527240 1914.411    0.000 1914.411    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              143278405 1895.928    0.000 1895.928    0.000 {built-in method clone}
               97853700   79.821    0.000 1849.931    0.000 activation.py:713(forward)
               97853700   83.979    0.000 1770.111    0.000 functional.py:1364(leaky_relu)
              181527240 1672.390    0.000 1672.390    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               97853700 1669.362    0.000 1669.362    0.000 {built-in method torch._C._nn.leaky_relu}
               11417764   79.898    0.000 1668.120    0.000 agent.py:59(modify_board)
                3241554   60.797    0.000 1643.480    0.001 agent.py:171(__call__)
             6343158159 1094.966    0.000 1560.413    0.000 enum.py:646(__hash__)
                3241560   56.075    0.000 1536.888    0.000 agent.py:112(__call__)
                9724674  225.679    0.000 1426.773    0.000 optimizer.py:189(zero_grad)
              324303564  319.509    0.000 1387.897    0.000 {built-in method builtins.any}
                3241560 1041.415    0.000 1339.936    0.000 replaybuffer.py:73(CF_save_data)
              324156100  164.756    0.000 1252.590    0.000 {built-in method builtins.all}
              323908690  897.340    0.000 1183.268    0.000 layers.py:77(check)
             1952045239  490.418    0.000 1126.474    0.000 layers.py:690(<genexpr>)
              323908690  704.322    0.000 1095.063    0.000 layers.py:286(check)
                3094097   39.261    0.000 1088.291    0.000 layers.py:740(restart)
             3531682033  875.502    0.000 1068.388    0.000 layers.py:700(<genexpr>)
               11417764 1059.737    0.000 1059.737    0.000 {built-in method torch._C._nn.one_hot}
               90763620 1029.554    0.000 1029.554    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              323908690  594.411    0.000  983.319    0.000 layers.py:246(check)
             1081682756  921.728    0.000  921.728    0.000 layer.py:146(elements)
                3241560   64.060    0.000  888.857    0.000 replaybuffer.py:18(stacker)
               90763620  888.380    0.000  888.380    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3241554   70.764    0.000  864.996    0.000 replaybuffer.py:63(stacker)
               90763620  852.651    0.000  852.651    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               90763620  838.893    0.000  838.893    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3094097   17.620    0.000  770.956    0.000 level.py:8(__init__)
             8382699516  723.820    0.000  723.820    0.000 layer.py:91(positions)
                3241560  406.400    0.000  672.593    0.000 collector.py:46(collect)
               90763620  655.974    0.000  655.974    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              323908690  489.881    0.000  640.652    0.000 layers.py:62(check)
                3094097  102.729    0.000  616.229    0.000 levels.py:199(generate)
                8176204  224.976    0.000  611.620    0.000 exploration.py:53(softmaxer)
        8549844932/8549844929  539.321    0.000  602.858    0.000 {built-in method builtins.len}
              324156100  371.645    0.000  553.314    0.000 layers.py:113(isDone)
                1700213  467.270    0.000  552.346    0.000 agent.py:186(convert_values)
              635345424  419.478    0.000  519.353    0.000 tensor.py:906(grad)
              323908690  323.998    0.000  502.075    0.000 layers.py:273(check)
              323908690  317.645    0.000  501.601    0.000 layers.py:313(check)
               12671314  184.861    0.000  483.963    0.000 random.py:315(sample)
              157937723  482.046    0.000  482.046    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9724674   13.787    0.000  472.555    0.000 loss.py:527(forward)
             6343195150  465.452    0.000  465.452    0.000 {built-in method builtins.hash}
                9724674   36.448    0.000  458.768    0.000 functional.py:2898(mse_loss)
                6188194   49.288    0.000  417.570    0.000 level.py:41(notUsed)
              323908690  279.323    0.000  415.056    0.000 layers.py:48(check)
              323908690  221.704    0.000  319.864    0.000 layers.py:23(check)
               52168410   35.605    0.000  302.782    0.000 flatten.py:39(forward)
                9724674  302.470    0.000  302.470    0.000 {built-in method torch._C._nn.mse_loss}
               19449360  284.558    0.000  284.558    0.000 {built-in method sum}
                6483122  283.729    0.000  283.729    0.000 {built-in method nonzero}
              295402730  199.916    0.000  276.083    0.000 layer.py:126(remove)
                9725815  271.861    0.000  271.861    0.000 {built-in method max}
               30940970   40.293    0.000  268.579    0.000 layer.py:69(restart)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533966: <Causal4_Cf_convert4_TopN6_2> in cluster <dcc> Done

Job <Causal4_Cf_convert4_TopN6_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 19 22:07:23 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 22:07:23 2021
Terminated at Tue Apr 20 22:02:45 2021
Results reported at Tue Apr 20 22:02:45 2021

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

    CPU time :                                   85901.12 sec.
    Max Memory :                                 9338 MB
    Average Memory :                             6210.81 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7046.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86123 sec.
    Turnaround time :                            178957 sec.

The output (if any) is above this job summary.

