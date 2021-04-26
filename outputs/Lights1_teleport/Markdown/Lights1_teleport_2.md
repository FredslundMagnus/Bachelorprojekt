
# Parameters

    Name :                      Lights1_teleport-2
    Main :                      teleport
    Level :                     Levels.Causal3
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


      79523887891 function calls (79257764504 primitive calls) in 86115.30 seconds

##    Ordered by: cumulative time
   List reduced from 478 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.296 86115.296 {built-in method builtins.exec}
                      1    1.460    1.460 86115.296 86115.296 <string>:1(<module>)
                      1  210.113  210.113 86113.836 86113.836 main.py:45(teleport)
                9509030   33.863    0.000 32603.668    0.003 agent.py:29(learn)
                9509030  776.590    0.000 27933.295    0.003 learner.py:42(Qlearn)
                4754515   19.962    0.000 21617.448    0.005 game.py:41(step)
                4754515   25.385    0.000 20473.894    0.004 layers.py:718(step)
                4754515  154.190    0.000 19603.661    0.004 agent.py:54(_learn)
                4754515  126.505    0.000 12947.751    0.003 agent.py:117(_learn)
        299393109/33270733 1121.764    0.000 12583.198    0.000 module.py:715(_call_impl)
                4754515  359.637    0.000 12579.595    0.003 layers.py:17(step)
              475451500  715.623    0.000 12180.979    0.000 layer.py:98(move)
                9509030   56.023    0.000 11920.955    0.001 grad_mode.py:23(decorate_context)
               23761703   57.561    0.000 11787.502    0.000 network.py:27(forward)
                9509030  303.307    0.000 11758.263    0.001 adam.py:55(step)
               23761703  286.658    0.000 11594.616    0.000 container.py:115(forward)
                9509030 2147.154    0.000 10162.400    0.001 functional.py:53(adam)
                4754515 4368.127    0.001 8390.694    0.002 replaybuffer.py:28(teleporter_save_data)
                4754515 4374.465    0.001 8217.711    0.002 agent.py:88(interveen)
                4754516  624.313    0.000 7836.144    0.002 layers.py:684(update)
                9498158  216.057    0.000 7760.880    0.001 agent.py:49(__call__)
              475451500 1573.489    0.000 7456.407    0.000 layers.py:735(check)
                9509030   55.216    0.000 6480.411    0.001 tensor.py:181(backward)
                9509030   31.563    0.000 6425.195    0.001 __init__.py:68(backward)
                9509030 6144.891    0.001 6144.891    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4754515 3548.074    0.001 5689.767    0.001 replaybuffer.py:22(sample_data)
                4754515 2778.061    0.001 5234.043    0.001 agent.py:67(modify)
               47523406   77.957    0.000 4211.890    0.000 conv.py:422(forward)
               47523406   92.359    0.000 4104.542    0.000 conv.py:414(_conv_forward)
               47523406 3996.803    0.000 3996.803    0.000 {built-in method conv2d}
               61776079  129.766    0.000 3785.151    0.000 linear.py:92(forward)
               61776079  232.356    0.000 3596.766    0.000 functional.py:1669(linear)
              475451500  728.105    0.000 3342.199    0.000 layers.py:729(isFree)
              227940125 3218.474    0.000 3218.474    0.000 {built-in method clone}
             3602183746 2085.591    0.000 2614.094    0.000 layer.py:95(isFree)
               61776079 2597.018    0.000 2597.018    0.000 {built-in method addmm}
                4754515   64.430    0.000 2428.921    0.001 agent.py:112(__call__)
              599068944 1548.350    0.000 2426.368    0.000 tensor.py:933(grad)
             1329835313  695.837    0.000 2406.202    0.000 {built-in method builtins.any}
                9509030  216.882    0.000 2371.712    0.000 optimizer.py:167(zero_grad)
               38036128 1350.659    0.000 2360.751    0.000 layer.py:167(NoRock_update)
               14252673  102.264    0.000 2336.117    0.000 agent.py:59(modify_board)
               38025248 2247.605    0.000 2247.605    0.000 {built-in method cat}
              171162540 2126.602    0.000 2126.602    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6120050   57.412    0.000 1859.342    0.000 layers.py:740(restart)
                4754515   76.286    0.000 1817.680    0.000 replaybuffer.py:18(stacker)
              171162540 1802.855    0.000 1802.855    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               85537782   70.905    0.000 1756.085    0.000 activation.py:713(forward)
             6970102106 1187.006    0.000 1694.949    0.000 enum.py:646(__hash__)
               85537782  103.549    0.000 1685.179    0.000 functional.py:1292(leaky_relu)
               20305458 1582.881    0.000 1582.881    0.000 {built-in method tensor}
               85537782 1571.185    0.000 1571.185    0.000 {built-in method torch._C._nn.leaky_relu}
              475451500  921.786    0.000 1495.818    0.000 layers.py:286(check)
               14252673 1473.257    0.000 1473.257    0.000 {built-in method torch._C._nn.one_hot}
              475451500  853.793    0.000 1419.944    0.000 layers.py:246(check)
                6120050   29.394    0.000 1324.986    0.000 level.py:8(__init__)
             4223983950 1034.364    0.000 1267.722    0.000 layers.py:700(<genexpr>)
               33284189  178.154    0.000 1263.885    0.000 tensor.py:21(wrapped)
                9509030   11.035    0.000 1210.452    0.000 game.py:37(board)
              508735789  197.642    0.000 1197.073    0.000 {built-in method builtins.all}
              779709623  406.923    0.000 1196.179    0.000 overrides.py:1070(has_torch_function)
               85581270 1167.271    0.000 1167.271    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4754515  675.308    0.000 1131.518    0.000 collector.py:46(collect)
               85581270 1057.571    0.000 1057.571    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             2085254975  494.668    0.000 1032.257    0.000 layers.py:690(<genexpr>)
                6120050  116.050    0.000 1016.530    0.000 levels.py:164(generate)
              242192798  982.536    0.000  982.536    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               85581270  962.325    0.000  962.325    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               85581270  872.481    0.000  872.481    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9498158  298.862    0.000  837.188    0.000 exploration.py:53(softmaxer)
              475451500  496.281    0.000  781.856    0.000 layers.py:273(check)
             8826653526  773.216    0.000  773.216    0.000 layer.py:91(positions)
               12240100  106.701    0.000  740.699    0.000 level.py:41(notUsed)
              475451500  463.325    0.000  731.487    0.000 layers.py:313(check)
               85581270  684.462    0.000  684.462    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1567594494  608.320    0.000  608.320    0.000 layer.py:146(elements)
              475451500  401.853    0.000  604.666    0.000 layers.py:48(check)
                9509030   15.043    0.000  535.620    0.000 loss.py:445(forward)
               23772575  526.992    0.000  526.992    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                9509030   48.384    0.000  520.577    0.000 functional.py:2637(mse_loss)
        5535325667/5535325665  380.635    0.000  518.850    0.000 {built-in method builtins.len}
             6970136705  507.949    0.000  507.949    0.000 {built-in method builtins.hash}
               61776079  497.994    0.000  497.994    0.000 {method 't' of 'torch._C._TensorBase' objects}
              475451500  333.311    0.000  486.829    0.000 layers.py:23(check)
               48960400   57.354    0.000  461.023    0.000 layer.py:69(restart)
               28527090  453.632    0.000  453.632    0.000 {built-in method sum}
             1654478565  346.722    0.000  436.733    0.000 overrides.py:1083(<genexpr>)
               16994615  161.928    0.000  428.372    0.000 random.py:315(sample)
              748100283  294.485    0.000  400.604    0.000 layer.py:130(add)
                9509030  330.935    0.000  330.935    0.000 {built-in method torch._C._nn.mse_loss}
             4311967806  328.535    0.000  328.535    0.000 {method 'random' of '_random.Random' objects}
               47523406   34.473    0.000  327.680    0.000 flatten.py:39(forward)
              435974935  206.926    0.000  309.178    0.000 layer.py:126(remove)
                4756413  304.254    0.000  304.254    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               12240100   11.409    0.000  296.819    0.000 level.py:38(elementsIn)
                9510454  296.610    0.000  296.610    0.000 {built-in method max}
              169296447  199.412    0.000  294.655    0.000 layers.py:113(isDone)
               47523406  293.207    0.000  293.207    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6120150  148.283    0.000  291.436    0.000 layers.py:36(reset)
             2656221584  269.768    0.000  269.768    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550891: <Lights1_teleport_2> in cluster <dcc> Done

Job <Lights1_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:47 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 21 07:12:14 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 07:12:14 2021
Terminated at Thu Apr 22 07:07:37 2021
Results reported at Thu Apr 22 07:07:37 2021

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

    CPU time :                                   85890.95 sec.
    Max Memory :                                 2682 MB
    Average Memory :                             2677.12 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13702.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86125 sec.
    Turnaround time :                            139550 sec.

The output (if any) is above this job summary.

