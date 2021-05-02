
# Parameters

    Name :                      Maze_Conver2-1
    Main :                      CFagent
    Level :                     Levels.Maze
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      61048078930 function calls (60717113903 primitive calls) in 86064.39 seconds

##    Ordered by: cumulative time
   List reduced from 517 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.214 86109.214 {built-in method builtins.exec}
                      1    4.513    4.513 86109.214 86109.214 <string>:1(<module>)
                      1  441.649  441.649 86104.701 86104.701 main.py:79(CFagent)
               10800945   49.244    0.000 28111.496    0.003 agent.py:29(learn)
               10800944  718.273    0.000 22688.421    0.002 learner.py:42(Qlearn)
                3600315   21.496    0.000 18133.324    0.005 game.py:41(step)
                3600315   25.031    0.000 17304.481    0.005 layers.py:718(step)
        370544663/39581327 1582.426    0.000 12710.609    0.000 module.py:866(_call_impl)
               28780383   82.819    0.000 11820.271    0.000 network.py:27(forward)
               28780383  392.444    0.000 11530.930    0.000 container.py:117(forward)
                3600315  436.065    0.000 10952.829    0.003 agent.py:54(_learn)
                3600315  427.699    0.000 9989.998    0.003 agent.py:204(_learn)
                3600315  351.025    0.000 9920.893    0.003 layers.py:17(step)
              359854157  626.168    0.000 9537.235    0.000 layer.py:98(move)
                3600315  743.796    0.000 8886.475    0.002 agent.py:212(counterfact)
               10800944  107.262    0.000 8744.406    0.001 optimizer.py:84(wrapper)
                3600315 7073.995    0.002 8286.003    0.002 replaybuffer.py:22(sample_data)
               10800944   57.534    0.000 8274.469    0.001 grad_mode.py:24(decorate_context)
               10800944  365.321    0.000 8093.314    0.001 adam.py:55(step)
                3600315 6733.390    0.002 7886.054    0.002 replaybuffer.py:67(sample_data)
                3600316  553.686    0.000 7321.716    0.002 layers.py:684(update)
               10800944 1669.412    0.000 7320.808    0.001 _functional.py:53(adam)
                3600315  114.723    0.000 7092.205    0.002 agent.py:117(_learn)
                8982980  264.803    0.000 6227.775    0.001 agent.py:49(__call__)
               10800944   45.577    0.000 5989.549    0.001 tensor.py:195(backward)
               10800944   52.407    0.000 5942.443    0.001 __init__.py:68(backward)
               10800944 5642.044    0.001 5642.044    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              359854157 1299.834    0.000 5340.412    0.000 layers.py:735(check)
               48984108 4405.140    0.000 4405.140    0.000 {built-in method tensor}
               57560766  132.789    0.000 4289.869    0.000 conv.py:398(forward)
                3600315 1788.892    0.000 4217.785    0.001 agent.py:88(interveen)
               40723716   28.377    0.000 4189.154    0.000 game.py:37(board)
               57560766   86.697    0.000 4090.456    0.000 conv.py:390(_conv_forward)
               57605048 2273.583    0.000 4050.976    0.000 layer.py:167(NoRock_update)
               57560766 4003.759    0.000 4003.759    0.000 {built-in method conv2d}
                3600315 1974.416    0.001 3409.819    0.001 replaybuffer.py:28(teleporter_save_data)
               79140519  163.055    0.000 3247.133    0.000 linear.py:93(forward)
              359854157  503.759    0.000 3046.763    0.000 layers.py:729(isFree)
               79140519   66.166    0.000 2995.813    0.000 functional.py:1737(linear)
               79140519 2913.077    0.000 2913.077    0.000 {built-in method torch._C._nn.linear}
                3600315 1828.617    0.001 2808.589    0.001 agent.py:67(modify)
             2287197520 2186.091    0.000 2543.004    0.000 layer.py:95(isFree)
                1795830   38.559    0.000 2514.135    0.001 agent.py:176(choose_action)
                2924736   48.040    0.000 2342.454    0.001 layers.py:740(restart)
                2924736   29.508    0.000 2017.018    0.001 level.py:8(__init__)
               48586440 1936.535    0.000 1936.535    0.000 {built-in method cat}
                3986061  259.073    0.000 1798.350    0.000 levels.py:9(generate)
               12583295   99.817    0.000 1794.686    0.000 agent.py:59(modify_board)
                3600314   72.475    0.000 1747.074    0.000 agent.py:172(__call__)
              107920902   93.532    0.000 1691.983    0.000 activation.py:713(forward)
              107920902   91.249    0.000 1598.451    0.000 functional.py:1364(leaky_relu)
                3600315   68.316    0.000 1576.979    0.000 agent.py:112(__call__)
              359854157  965.209    0.000 1559.271    0.000 layers.py:168(check)
              107920902 1489.648    0.000 1489.648    0.000 {built-in method torch._C._nn.leaky_relu}
              201617620 1427.607    0.000 1427.607    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              136399030 1422.614    0.000 1422.614    0.000 {built-in method clone}
              360707180  322.519    0.000 1343.270    0.000 {built-in method builtins.any}
               10800944  237.642    0.000 1310.265    0.000 optimizer.py:189(zero_grad)
              201617620 1260.004    0.000 1260.004    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3600315  972.605    0.000 1209.921    0.000 replaybuffer.py:73(CF_save_data)
               12583295 1179.788    0.000 1179.788    0.000 {built-in method torch._C._nn.one_hot}
             1210278298 1067.454    0.000 1067.454    0.000 layer.py:146(elements)
             3680955227  710.488    0.000 1046.998    0.000 enum.py:646(__hash__)
             3213961776  841.596    0.000 1020.751    0.000 layers.py:700(<genexpr>)
                3600315   71.933    0.000  914.605    0.000 replaybuffer.py:18(stacker)
                3600314   68.365    0.000  866.342    0.000 replaybuffer.py:63(stacker)
              360031600  150.286    0.000  860.566    0.000 {built-in method builtins.all}
              100808810  840.876    0.000  840.876    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1614573562  425.578    0.000  755.256    0.000 layers.py:690(<genexpr>)
              100808810  732.196    0.000  732.196    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              100808810  687.819    0.000  687.819    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              100808810  672.386    0.000  672.386    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               18097488  253.767    0.000  653.988    0.000 random.py:315(sample)
                8982980  229.636    0.000  653.695    0.000 exploration.py:53(softmaxer)
              705661754  527.230    0.000  647.385    0.000 tensor.py:906(grad)
        7961833997/7961833994  561.559    0.000  636.877    0.000 {built-in method builtins.len}
              359854157  394.265    0.000  627.566    0.000 layers.py:141(check)
                8774208   75.893    0.000  621.399    0.000 level.py:41(notUsed)
              359854157  404.250    0.000  573.784    0.000 layers.py:48(check)
              359854157  385.843    0.000  572.625    0.000 layers.py:124(check)
                3600315  327.294    0.000  564.268    0.000 collector.py:46(collect)
                3986061  291.892    0.000  547.208    0.000 levels.py:75(RFS)
               10800944   24.075    0.000  536.246    0.000 loss.py:527(forward)
             5731774293  523.143    0.000  523.143    0.000 layer.py:91(positions)
               10800944   53.565    0.000  512.171    0.000 functional.py:2898(mse_loss)
              100808810  498.719    0.000  498.719    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1795830  402.838    0.000  457.392    0.000 agent.py:187(convert_values)
              359854157  264.517    0.000  393.590    0.000 layers.py:23(check)
              548286781  244.729    0.000  338.816    0.000 layer.py:130(add)
             3680996250  336.518    0.000  336.518    0.000 {built-in method builtins.hash}
              381062603  229.419    0.000  329.505    0.000 layer.py:126(remove)
              152582639  326.277    0.000  326.277    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              457435459  212.810    0.000  316.533    0.000 random.py:250(_randbelow_with_getrandbits)
                7200632  308.406    0.000  308.406    0.000 {built-in method nonzero}
               10800944  307.704    0.000  307.704    0.000 {built-in method torch._C._nn.mse_loss}
               57560766   43.000    0.000  280.630    0.000 flatten.py:39(forward)
               10802202  278.413    0.000  278.413    0.000 {built-in method max}
              292165623  271.183    0.000  271.183    0.000 level.py:32(inverse)
               23397888   35.907    0.000  269.087    0.000 layer.py:69(restart)
             3242465071  256.532    0.000  256.532    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579176: <Maze_Conver2_1> in cluster <dcc> Done

Job <Maze_Conver2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:08 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat May  1 16:34:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  1 16:34:09 2021
Terminated at Sun May  2 16:29:25 2021
Results reported at Sun May  2 16:29:25 2021

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

    CPU time :                                   85903.59 sec.
    Max Memory :                                 9746 MB
    Average Memory :                             6461.51 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6638.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86118 sec.
    Turnaround time :                            481517 sec.

The output (if any) is above this job summary.

