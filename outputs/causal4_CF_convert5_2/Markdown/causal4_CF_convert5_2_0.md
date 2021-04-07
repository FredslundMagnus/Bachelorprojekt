
# Parameters

    Name :                      causal4_CF_convert5_2-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                5
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      58348423127 function calls (58024141376 primitive calls) in 86116.46 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86116.458 86116.458 {built-in method builtins.exec}
                      1    4.997    4.997 86116.458 86116.458 <string>:1(<module>)
                      1  269.032  269.032 86111.461 86111.461 main.py:96(CFagent)
               10717044   43.363    0.000 32035.398    0.003 agent.py:29(learn)
               10717036  807.800    0.000 26616.501    0.002 learner.py:42(Qlearn)
                3572348   18.417    0.000 16966.480    0.005 game.py:35(step)
                3572348   20.862    0.000 16075.654    0.005 layers.py:448(step)
        363211217/38931157 1495.251    0.000 13417.413    0.000 module.py:866(_call_impl)
               28214121   80.997    0.000 12572.588    0.000 network.py:24(forward)
                3572348  388.281    0.000 12379.563    0.003 agent.py:54(_learn)
               28214121  382.841    0.000 12312.350    0.000 container.py:117(forward)
                3572348  321.599    0.000 11647.183    0.003 layers.py:17(step)
                3572348  387.746    0.000 11459.309    0.003 agent.py:196(_learn)
              356958198  876.701    0.000 11292.752    0.000 layer.py:84(move)
               10717036   92.184    0.000 11242.117    0.001 optimizer.py:84(wrapper)
                3572348  901.851    0.000 10815.721    0.003 agent.py:204(counterfact)
               10717036   46.012    0.000 10805.340    0.001 grad_mode.py:24(decorate_context)
               10717036  321.109    0.000 10658.924    0.001 adam.py:55(step)
               10717036 2196.298    0.000 9994.494    0.001 _functional.py:53(adam)
                3572348  111.711    0.000 8129.301    0.002 agent.py:115(_learn)
               10717036   45.317    0.000 6656.859    0.001 tensor.py:195(backward)
               10717036   44.578    0.000 6609.986    0.001 __init__.py:68(backward)
              356958198 1074.853    0.000 6459.517    0.000 layers.py:465(check)
                8738906  243.320    0.000 6352.057    0.001 agent.py:49(__call__)
               10717036 6329.183    0.001 6329.183    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               55589845 5866.910    0.000 5866.910    0.000 {built-in method tensor}
               47390313   34.854    0.000 5630.595    0.000 game.py:31(board)
                3572348 4159.514    0.001 5489.156    0.002 replaybuffer.py:22(sample_data)
                3572348 2563.036    0.001 4786.628    0.001 replaybuffer.py:28(teleporter_save_data)
                3572348 3598.336    0.001 4752.983    0.001 replaybuffer.py:49(sample_data)
                3572348 2065.393    0.001 4632.372    0.001 agent.py:86(interveen)
               71446970 2683.048    0.000 4587.623    0.000 layer.py:129(update)
               56428242  120.863    0.000 4459.912    0.000 conv.py:398(forward)
                3572349  378.328    0.000 4374.471    0.001 layers.py:419(update)
               56428242   79.388    0.000 4280.405    0.000 conv.py:390(_conv_forward)
               56428242 4201.017    0.000 4201.017    0.000 {built-in method conv2d}
               77497667  157.053    0.000 3568.804    0.000 linear.py:93(forward)
              356774636  619.466    0.000 3383.199    0.000 layers.py:459(isFree)
               77497667   63.570    0.000 3332.186    0.000 functional.py:1737(linear)
               77497667 3252.410    0.000 3252.410    0.000 {built-in method torch._C._nn.linear}
             3155086472 2292.411    0.000 2763.733    0.000 layer.py:81(isFree)
                3572348 1626.919    0.000 2727.524    0.001 agent.py:67(modify)
                1613491   37.359    0.000 2473.519    0.002 agent.py:168(choose_action)
               51607042 2161.847    0.000 2161.847    0.000 {built-in method cat}
              158378940 2089.444    0.000 2089.444    0.000 {built-in method clone}
              200051328 2056.054    0.000 2056.054    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              105711788   81.745    0.000 1972.775    0.000 activation.py:713(forward)
              105711788   90.742    0.000 1891.031    0.000 functional.py:1364(leaky_relu)
                3572340   68.771    0.000 1808.324    0.001 agent.py:164(__call__)
              200051328 1788.642    0.000 1788.642    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              105711788 1780.685    0.000 1780.685    0.000 {built-in method torch._C._nn.leaky_relu}
               12311254   83.471    0.000 1780.632    0.000 agent.py:59(modify_board)
                3572348   64.758    0.000 1699.824    0.000 agent.py:110(__call__)
               10717036  248.004    0.000 1541.560    0.000 optimizer.py:189(zero_grad)
             5787268623  948.756    0.000 1352.451    0.000 enum.py:646(__hash__)
               12311254 1133.314    0.000 1133.314    0.000 {built-in method torch._C._nn.one_hot}
              100025664 1108.787    0.000 1108.787    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              356958198  706.731    0.000 1092.008    0.000 layers.py:233(check)
             1120342465 1084.059    0.000 1084.059    0.000 layer.py:124(elements)
                3572348   83.461    0.000 1080.289    0.000 replaybuffer.py:18(stacker)
              356958198  608.771    0.000 1002.035    0.000 layers.py:270(check)
              100025664  976.484    0.000  976.484    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              356958198  745.033    0.000  956.928    0.000 layers.py:67(check)
                2908646   34.749    0.000  928.901    0.000 layers.py:469(restart)
              100025664  925.548    0.000  925.548    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              100025664  914.190    0.000  914.190    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3572340   74.026    0.000  913.299    0.000 replaybuffer.py:45(stacker)
                3572348  301.926    0.000  782.307    0.000 replaybuffer.py:55(CF_save_data)
                3572348  441.862    0.000  732.474    0.000 collector.py:54(collect)
              100025664  704.291    0.000  704.291    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              356958198  551.327    0.000  702.146    0.000 layers.py:56(check)
             7950077955  672.306    0.000  672.306    0.000 layer.py:77(positions)
                8738906  239.311    0.000  664.949    0.000 exploration.py:53(softmaxer)
                2908646   17.668    0.000  632.586    0.000 level.py:8(__init__)
        8747196980/8747196977  543.718    0.000  611.805    0.000 {built-in method builtins.len}
              356958198  376.354    0.000  575.630    0.000 layers.py:294(check)
              700179732  455.323    0.000  565.420    0.000 tensor.py:906(grad)
              357234900   93.163    0.000  547.819    0.000 {built-in method builtins.all}
              174262534  536.390    0.000  536.390    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               10717036   16.670    0.000  521.865    0.000 loss.py:527(forward)
               12961988  197.704    0.000  521.204    0.000 random.py:315(sample)
              356958198  327.245    0.000  515.084    0.000 layers.py:257(check)
                2908646   93.430    0.000  513.613    0.000 levels.py:199(generate)
               10717036   40.910    0.000  505.195    0.000 functional.py:2898(mse_loss)
             1128652291  252.967    0.000  493.142    0.000 layers.py:425(<genexpr>)
               10717045  471.965    0.000  471.965    0.000 {built-in method nonzero}
                1613491  398.784    0.000  458.141    0.000 agent.py:179(convert_values)
              356958198  309.466    0.000  456.056    0.000 layers.py:42(check)
             5787309310  403.702    0.000  403.702    0.000 {built-in method builtins.hash}
               10717036  332.673    0.000  332.673    0.000 {built-in method torch._C._nn.mse_loss}
                5817292   41.120    0.000  330.849    0.000 level.py:41(notUsed)
               56428242   36.932    0.000  322.646    0.000 flatten.py:39(forward)
               21434088  309.394    0.000  309.394    0.000 {built-in method sum}
              317781169  216.993    0.000  303.653    0.000 layer.py:104(remove)
               10718266  299.160    0.000  299.160    0.000 {built-in method max}
               15902875   24.178    0.000  290.496    0.000 tensor.py:525(__rsub__)
               56428242  285.714    0.000  285.714    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               71446970  275.378    0.000  275.378    0.000 layer.py:141(<listcomp>)
              489407817  190.947    0.000  263.791    0.000 layer.py:108(add)
               15902875  262.511    0.000  262.511    0.000 {built-in method rsub}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9496010: <causal4_CF_convert5_2_0> in cluster <dcc> Done

Job <causal4_CF_convert5_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 20:00:35 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr  6 02:46:22 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr  6 02:46:22 2021
Terminated at Wed Apr  7 02:41:46 2021
Results reported at Wed Apr  7 02:41:46 2021

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

    CPU time :                                   85892.39 sec.
    Max Memory :                                 10384 MB
    Average Memory :                             6956.64 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6000.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86124 sec.
    Turnaround time :                            110471 sec.

The output (if any) is above this job summary.

